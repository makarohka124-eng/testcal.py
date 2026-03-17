// testcal.jsx — Logist Calc
// Requires: React, shadcn/ui, lucide-react, date-fns
// shadcn components used: Card, Label, Input, Slider, Switch, Select, RadioGroup, Badge, Button, Separator, Alert

import { useState, useMemo, useEffect } from "react"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { Slider } from "@/components/ui/slider"
import { Switch } from "@/components/ui/switch"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Separator } from "@/components/ui/separator"
import { Alert, AlertDescription } from "@/components/ui/alert"
import { Truck, Clock, Copy, Check, AlertTriangle, CheckCircle2, Moon, Sun } from "lucide-react"

// ─── helpers ────────────────────────────────────────────────────────────────

function getCETNow() {
  return new Date(new Date().toLocaleString("en-US", { timeZone: "Europe/Berlin" }))
}

function pad(n) {
  return String(n).padStart(2, "0")
}

function todayISO() {
  const d = getCETNow()
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`
}

function tomorrowISO() {
  const d = getCETNow()
  d.setDate(d.getDate() + 1)
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`
}

function nowTimeStr() {
  const d = getCETNow()
  return `${pad(d.getHours())}:${pad(d.getMinutes())}`
}

function localeDateRu(date) {
  return date.toLocaleString("ru-RU", {
    timeZone: "Europe/Berlin",
    weekday: "long",
    day: "2-digit",
    month: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    hour12: false,
  })
}

function calcArrival({
  useCurrent, startDate, startTime,
  dist, speed, mode, alreadyDriven,
  gas, trailer, loading, ferry, misc,
}) {
  const startDt = useCurrent
    ? getCETNow()
    : new Date(`${startDate}T${startTime}:00`)

  const extra =
    (gas ? 1 : 0) +
    (trailer ? 1 : 0) +
    (loading ? 2 : 0) +
    Number(misc) +
    Number(ferry)

  const pureDrive = dist / speed
  const limit = mode === "single" ? 9.0 : 18.0
  const currentLeft = Math.max(0, limit - alreadyDriven)

  let totalWay, driveRemaining

  if (mode === "single") {
    if (pureDrive <= currentLeft) {
      const needBreak = alreadyDriven < 4.5 && alreadyDriven + pureDrive > 4.5 ? 1 : 0
      totalWay = pureDrive + needBreak
      driveRemaining = currentLeft - pureDrive
    } else {
      const rem = pureDrive - currentLeft
      const shifts = Math.ceil(rem / 9)
      totalWay =
        pureDrive +
        shifts * 9 +
        (alreadyDriven < 4.5 ? 1 : 0) +
        shifts * 2
      driveRemaining = rem % 9 !== 0 ? 9 - (rem % 9) : 9
    }
  } else {
    const shifts =
      pureDrive > currentLeft ? Math.ceil((pureDrive - currentLeft) / 18) : 0
    totalWay = pureDrive + shifts * 9
    driveRemaining =
      shifts === 0
        ? currentLeft - pureDrive
        : 18 - ((pureDrive - currentLeft) % 18)
  }

  totalWay += extra

  const arrival = new Date(startDt.getTime() + totalWay * 3600_000)

  const cetNow = getCETNow()
  const checkVal = cetNow.getHours() < 12 ? "1/2" : "2/2"

  // format arrival in CET for work string
  const a = new Date(
    arrival.toLocaleString("en-US", { timeZone: "Europe/Berlin" })
  )
  const dd = pad(a.getDate())
  const mm = pad(a.getMonth() + 1)
  const hh = pad(a.getHours())
  const min = pad(a.getMinutes())
  const workString = `${checkVal} ETA ${dd}.${mm} ${hh}:${min}CET D/H ${Math.floor(driveRemaining)}`

  return {
    arrival,
    workString,
    driveRemaining,
    pureDrive: pureDrive.toFixed(1),
    totalWay: totalWay.toFixed(1),
    extra,
  }
}

// ─── component ───────────────────────────────────────────────────────────────

export default function LogistCalc() {
  const now = getCETNow()

  // departure
  const [useCurrent, setUseCurrent] = useState(true)
  const [startDate, setStartDate] = useState(todayISO())
  const [startTime, setStartTime] = useState(nowTimeStr())

  // route
  const [dist, setDist] = useState(1000)
  const [speed, setSpeed] = useState([70])
  const [mode, setMode] = useState("single")
  const [alreadyDriven, setAlreadyDriven] = useState(0)

  // fix time
  const [useFix, setUseFix] = useState(false)
  const [fixDate, setFixDate] = useState(tomorrowISO())
  const [fixTime, setFixTime] = useState("08:00")

  // extras
  const [gas, setGas] = useState(false)
  const [trailer, setTrailer] = useState(false)
  const [loading, setLoading] = useState(false)
  const [ferry, setFerry] = useState("0")
  const [misc, setMisc] = useState("0")

  const [copied, setCopied] = useState(false)
  const [dark, setDark] = useState(
    () => document.documentElement.classList.contains("dark") ||
      window.matchMedia("(prefers-color-scheme: dark)").matches
  )

  useEffect(() => {
    document.documentElement.classList.toggle("dark", dark)
  }, [dark])

  const maxDrive = mode === "single" ? 9 : 18

  const result = useMemo(
    () =>
      calcArrival({
        useCurrent, startDate, startTime,
        dist, speed: speed[0], mode, alreadyDriven,
        gas, trailer, loading, ferry, misc,
      }),
    [useCurrent, startDate, startTime, dist, speed, mode, alreadyDriven, gas, trailer, loading, ferry, misc]
  )

  const arrivalLabel = useMemo(() => localeDateRu(result.arrival), [result.arrival])

  // fix diff
  const fixDiff = useMemo(() => {
    if (!useFix) return null
    const fixDt = new Date(`${fixDate}T${fixTime}:00`)
    return (fixDt.getTime() - result.arrival.getTime()) / 3_600_000
  }, [useFix, fixDate, fixTime, result.arrival])

  const fixH = fixDiff !== null ? Math.floor(Math.abs(fixDiff)) : 0
  const fixM = fixDiff !== null ? Math.round((Math.abs(fixDiff) % 1) * 60) : 0
  const fixOk = fixDiff !== null && fixDiff >= 0

  function copyString() {
    navigator.clipboard.writeText(result.workString).then(() => {
      setCopied(true)
      setTimeout(() => setCopied(false), 1500)
    })
  }

  return (
    <div className="min-h-screen bg-background p-4 md:p-8">
      <div className="max-w-3xl mx-auto space-y-4">

        {/* Header */}
        <div className="flex items-center gap-3 mb-6">
          <div className="p-2 rounded-lg bg-primary text-primary-foreground">
            <Truck className="w-5 h-5" />
          </div>
          <div className="flex-1">
            <h1 className="text-xl font-semibold leading-none">Калькулятор рейса</h1>
            <p className="text-sm text-foreground mt-1">Логистика · CET</p>
          </div>
          <Button
            variant="outline"
            size="icon"
            onClick={() => setDark((d) => !d)}
            className="rounded-full w-9 h-9 shrink-0"
            aria-label="Переключить тему"
          >
            {dark ? <Sun className="w-4 h-4" /> : <Moon className="w-4 h-4" />}
          </Button>
        </div>

        {/* Departure */}
        <Card>
          <CardHeader className="pb-3">
            <CardTitle className="text-sm font-medium text-foreground uppercase tracking-wide">
              Время выезда
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="flex items-center gap-3">
              <Switch
                id="use-current"
                checked={useCurrent}
                onCheckedChange={setUseCurrent}
              />
              <Label htmlFor="use-current" className="cursor-pointer">
                Сейчас —{" "}
                <span className="text-foreground">
                  {pad(now.getHours())}:{pad(now.getMinutes())} · {pad(now.getDate())}.{pad(now.getMonth() + 1)}
                </span>
              </Label>
            </div>
            {!useCurrent && (
              <div className="grid grid-cols-2 gap-3">
                <div className="space-y-1.5">
                  <Label>Дата выезда</Label>
                  <Input
                    type="date"
                    value={startDate}
                    onChange={(e) => setStartDate(e.target.value)}
                  />
                </div>
                <div className="space-y-1.5">
                  <Label>Время (CET)</Label>
                  <Input
                    type="time"
                    value={startTime}
                    onChange={(e) => setStartTime(e.target.value)}
                  />
                </div>
              </div>
            )}
          </CardContent>
        </Card>

        <div className="grid md:grid-cols-2 gap-4">

          {/* Route params */}
          <Card>
            <CardHeader className="pb-3">
              <CardTitle className="text-sm font-medium text-foreground uppercase tracking-wide">
                Параметры рейса
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-5">
              <div className="space-y-1.5">
                <Label>Расстояние (км)</Label>
                <Input
                  type="number"
                  min={1}
                  value={dist}
                  onChange={(e) => setDist(Number(e.target.value))}
                />
              </div>

              <div className="space-y-3">
                <div className="flex justify-between">
                  <Label>Скорость</Label>
                  <span className="text-sm font-medium">{speed[0]} км/ч</span>
                </div>
                <Slider
                  min={40}
                  max={90}
                  step={1}
                  value={speed}
                  onValueChange={setSpeed}
                />
                <div className="flex justify-between text-xs text-foreground">
                  <span>40</span>
                  <span>90</span>
                </div>
              </div>

              <div className="space-y-1.5">
                <Label>Режим вождения</Label>
                <RadioGroup
                  value={mode}
                  onValueChange={setMode}
                  className="flex gap-4"
                >
                  <div className="flex items-center gap-2">
                    <RadioGroupItem value="single" id="single" />
                    <Label htmlFor="single" className="cursor-pointer font-normal">Одиночка</Label>
                  </div>
                  <div className="flex items-center gap-2">
                    <RadioGroupItem value="crew" id="crew" />
                    <Label htmlFor="crew" className="cursor-pointer font-normal">Экипаж</Label>
                  </div>
                </RadioGroup>
              </div>

              <div className="space-y-1.5">
                <div className="flex justify-between">
                  <Label>Уже проехал сегодня</Label>
                  <span className="text-xs text-foreground">макс {maxDrive}ч</span>
                </div>
                <Input
                  type="number"
                  min={0}
                  max={maxDrive}
                  step={0.5}
                  value={alreadyDriven}
                  onChange={(e) =>
                    setAlreadyDriven(Math.min(maxDrive, Number(e.target.value)))
                  }
                />
              </div>
            </CardContent>
          </Card>

          {/* Extras */}
          <Card>
            <CardHeader className="pb-3">
              <CardTitle className="text-sm font-medium text-foreground uppercase tracking-wide">
                Дополнительно
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="space-y-3">
                <div className="flex items-center gap-3">
                  <Switch
                    id="use-fix"
                    checked={useFix}
                    onCheckedChange={setUseFix}
                  />
                  <Label htmlFor="use-fix" className="cursor-pointer">Фикс время выгрузки</Label>
                </div>
                {useFix && (
                  <div className="grid grid-cols-2 gap-3 pl-9">
                    <div className="space-y-1.5">
                      <Label className="text-xs">Дата FIX</Label>
                      <Input
                        type="date"
                        value={fixDate}
                        onChange={(e) => setFixDate(e.target.value)}
                      />
                    </div>
                    <div className="space-y-1.5">
                      <Label className="text-xs">Время FIX</Label>
                      <Input
                        type="time"
                        value={fixTime}
                        onChange={(e) => setFixTime(e.target.value)}
                      />
                    </div>
                  </div>
                )}
              </div>

              <Separator />

              <div className="space-y-1">
                <Label className="text-xs text-foreground uppercase tracking-wide mb-2 block">Остановки</Label>
                {[
                  { id: "gas", label: "Заправка", extra: "+1ч", value: gas, set: setGas },
                  { id: "trailer", label: "Перецеп", extra: "+1ч", value: trailer, set: setTrailer },
                  { id: "loading", label: "Загрузка", extra: "+2ч", value: loading, set: setLoading },
                ].map(({ id, label, extra, value, set }) => (
                  <div key={id} className="flex items-center gap-3 py-1">
                    <Switch id={id} checked={value} onCheckedChange={set} />
                    <Label htmlFor={id} className="cursor-pointer font-normal flex gap-2 items-center">
                      {label}
                      <Badge variant="secondary" className="text-xs">{extra}</Badge>
                    </Label>
                  </div>
                ))}
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div className="space-y-1.5">
                  <Label>Паром</Label>
                  <Select value={ferry} onValueChange={setFerry}>
                    <SelectTrigger>
                      <SelectValue />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="0">Нет</SelectItem>
                      <SelectItem value="1">1 час</SelectItem>
                      <SelectItem value="2">2 часа</SelectItem>
                    </SelectContent>
                  </Select>
                </div>
                <div className="space-y-1.5">
                  <Label>Другое (ч)</Label>
                  <Select value={misc} onValueChange={setMisc}>
                    <SelectTrigger>
                      <SelectValue />
                    </SelectTrigger>
                    <SelectContent>
                      {[0, 1, 2, 3, 4, 5].map((v) => (
                        <SelectItem key={v} value={String(v)}>{v}</SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Result */}
        <Card>
          <CardHeader className="pb-3">
            <CardTitle className="text-sm font-medium text-foreground uppercase tracking-wide">
              Результат
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="grid md:grid-cols-2 gap-6">
              <div>
                <p className="text-xs text-foreground mb-1">Расчётное прибытие</p>
                <p className="text-2xl font-semibold leading-tight">{arrivalLabel}</p>

                {useFix && fixDiff !== null && (
                  <Alert
                    variant={fixOk ? "default" : "destructive"}
                    className="mt-3"
                  >
                    {fixOk
                      ? <CheckCircle2 className="h-4 w-4" />
                      : <AlertTriangle className="h-4 w-4" />}
                    <AlertDescription>
                      {fixOk
                        ? `Запас: ${fixH}ч ${fixM}м`
                        : `Опоздание: ${fixH}ч ${fixM}м`}
                    </AlertDescription>
                  </Alert>
                )}
              </div>

              <div className="space-y-2 text-sm">
                {[
                  ["Чистое время езды", `${result.pureDrive} ч`],
                  ["Итоговое время", `${result.totalWay} ч`],
                  ["Допы", `${result.extra} ч`],
                  ["Остаток вождения", `${Math.floor(result.driveRemaining)} ч`],
                ].map(([label, value]) => (
                  <div key={label} className="flex justify-between py-1.5 border-b last:border-0">
                    <span className="text-foreground">{label}</span>
                    <span className="font-medium">{value}</span>
                  </div>
                ))}
              </div>
            </div>

            <Separator />

            <div>
              <p className="text-xs text-foreground mb-2">Строка для отчёта</p>
              <div className="flex items-center gap-2 bg-muted rounded-md px-3 py-2.5">
                <Clock className="w-3.5 h-3.5 text-foreground shrink-0" />
                <code className="flex-1 text-sm font-mono">{result.workString}</code>
                <Button
                  size="sm"
                  variant="ghost"
                  className="h-7 px-2 gap-1.5"
                  onClick={copyString}
                >
                  {copied
                    ? <><Check className="w-3.5 h-3.5" /> Скопировано</>
                    : <><Copy className="w-3.5 h-3.5" /> Копировать</>}
                </Button>
              </div>
            </div>
          </CardContent>
        </Card>

        <p className="text-xs text-foreground text-right">
          Разработал Yaroslav Makarovskyi
        </p>
      </div>
    </div>
  )
}
