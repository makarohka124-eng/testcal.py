import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Logist Calc", layout="centered", page_icon="🚛")
st.markdown("""
<style>
  #MainMenu, footer, header { visibility: hidden; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#fff;--bg2:#f4f4f5;--bg3:#e4e4e7;
  --fg:#09090b;--fg2:#52525b;
  --border:rgba(0,0,0,0.12);--border2:rgba(0,0,0,0.22);
  --radius:8px;--radius-lg:12px;
  --card-bg:#fff;--muted-bg:#f4f4f5;
  --success-bg:#f0fdf4;--success-fg:#166534;--success-border:#bbf7d0;
  --danger-bg:#fef2f2;--danger-fg:#991b1b;--danger-border:#fecaca;
  --badge-bg:#e4e4e7;--badge-fg:#3f3f46;
  --primary:#09090b;--primary-fg:#fafafa;
}
.dark{
  --bg:#09090b;--bg2:#18181b;--bg3:#27272a;
  --fg:#fafafa;--fg2:#a1a1aa;
  --border:rgba(255,255,255,0.1);--border2:rgba(255,255,255,0.18);
  --card-bg:#18181b;--muted-bg:#27272a;
  --success-bg:#052e16;--success-fg:#86efac;--success-border:#166534;
  --danger-bg:#450a0a;--danger-fg:#fca5a5;--danger-border:#991b1b;
  --badge-bg:#3f3f46;--badge-fg:#d4d4d8;
  --primary:#fafafa;--primary-fg:#09090b;
}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:var(--bg);color:var(--fg);font-size:14px;transition:background .2s,color .2s}
.app{max-width:1100px;margin:0 auto;padding:24px 16px 48px}
.card{background:var(--card-bg);border:0.5px solid var(--border);border-radius:var(--radius-lg);padding:16px 20px;margin-bottom:12px;transition:background .2s,border-color .2s}
.card-title{font-size:11px;font-weight:500;color:var(--fg);letter-spacing:.08em;text-transform:uppercase;margin-bottom:14px}
.main-layout{display:grid;grid-template-columns:420px 1fr;gap:12px;align-items:start}
.combined-card{background:var(--card-bg);border:0.5px solid var(--border);border-radius:var(--radius-lg);padding:16px 20px;transition:background .2s,border-color .2s}
.section-sep{height:0.5px;background:var(--border);margin:16px 0}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}
.space-y>*+*{margin-top:14px}
.space-y-sm>*+*{margin-top:8px}
.flex-bw{display:flex;align-items:center;justify-content:space-between}
.flex-row{display:flex;align-items:center;gap:8px}
.mt-4{margin-top:4px}.mt-8{margin-top:8px}.mt-12{margin-top:12px}
.field-label{display:block;font-size:12px;color:var(--fg);margin-bottom:5px}
input[type=number],input[type=date],input[type=time],select,input[type=text]{
  width:100%;height:34px;padding:0 10px;
  background:var(--bg2);border:0.5px solid var(--border2);
  border-radius:var(--radius);color:var(--fg);font-size:13px;
  font-family:inherit;outline:none;transition:border-color .15s,box-shadow .15s;
}
input:focus,select:focus{border-color:var(--fg2);box-shadow:0 0 0 2px rgba(128,128,128,.15)}
input[type=range]{
  width:100%;accent-color:var(--fg);cursor:pointer;
  height:4px;background:transparent;
}

/* time slider block */
.time-slider-block{background:var(--bg2);border-radius:var(--radius);padding:12px 14px}
.time-display{font-size:22px;font-weight:600;font-family:monospace;color:var(--fg);text-align:center;margin-bottom:12px;letter-spacing:2px}
.slider-row{display:flex;align-items:center;gap:10px;margin-bottom:8px}
.slider-row:last-child{margin-bottom:0}
.slider-lbl{font-size:11px;color:var(--fg);width:30px;flex-shrink:0}
.slider-val{font-size:12px;font-weight:500;color:var(--fg);width:26px;text-align:right;flex-shrink:0}
.time-input-row{display:flex;gap:8px;margin-top:10px;align-items:center}
.time-input-row input[type=text]{text-align:center;font-family:monospace;font-size:14px;letter-spacing:1px}
.time-input-row span{font-size:12px;color:var(--fg);flex-shrink:0}

.switch{position:relative;width:36px;height:20px;flex-shrink:0}
.switch input{opacity:0;width:0;height:0}
.switch-track{position:absolute;inset:0;background:var(--border2);border-radius:100px;transition:background .2s;cursor:pointer}
.switch input:checked+.switch-track{background:#16a34a}
.switch-track::after{content:'';position:absolute;width:14px;height:14px;left:3px;top:3px;background:white;border-radius:50%;transition:transform .2s}
.switch input:checked+.switch-track::after{transform:translateX(16px)}
.switch-row{display:flex;align-items:center;gap:10px;cursor:pointer;user-select:none}

.radio-group{display:flex;gap:8px}
.radio-btn{flex:1;height:34px;display:flex;align-items:center;justify-content:center;border:0.5px solid var(--border2);border-radius:var(--radius);font-size:13px;cursor:pointer;background:var(--bg2);color:var(--fg);transition:all .15s;user-select:none}
.radio-btn.active{background:var(--primary);color:var(--primary-fg);border-color:var(--primary)}

.badge{display:inline-flex;align-items:center;padding:1px 7px;border-radius:100px;font-size:11px;font-weight:500;background:var(--badge-bg);color:var(--badge-fg)}
.tz-badge{display:inline-flex;align-items:center;padding:2px 8px;border-radius:100px;font-size:11px;font-weight:500;background:var(--primary);color:var(--primary-fg)}
.sep{height:0.5px;background:var(--border);margin:4px 0}

.alert{padding:10px 12px;border-radius:var(--radius);border:0.5px solid;font-size:13px;display:flex;align-items:center;gap:8px}
.alert-success{background:var(--success-bg);border-color:var(--success-border);color:var(--success-fg)}
.alert-danger{background:var(--danger-bg);border-color:var(--danger-border);color:var(--danger-fg)}

.stat-row{display:flex;justify-content:space-between;align-items:center;padding:6px 0;border-bottom:0.5px solid var(--border)}
.stat-row:last-child{border-bottom:none}
.stat-label{font-size:12px;color:var(--fg)}
.stat-value{font-size:13px;font-weight:500;color:var(--fg)}

.code-row{display:flex;align-items:center;gap:10px;background:var(--muted-bg);border-radius:var(--radius);padding:10px 12px}
.code-row code{flex:1;font-family:monospace;font-size:13px;color:var(--fg)}
.copy-btn{height:28px;padding:0 10px;flex-shrink:0;border:0.5px solid var(--border2);border-radius:var(--radius);background:var(--bg);color:var(--fg);font-size:12px;cursor:pointer;font-family:inherit;transition:background .1s}
.copy-btn:hover{background:var(--bg3)}

.header{display:flex;align-items:center;gap:12px;margin-bottom:20px}
.header-icon{width:36px;height:36px;border-radius:var(--radius);background:var(--primary);display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0}
.header-title{font-size:18px;font-weight:600;color:var(--fg)}
.header-sub{font-size:12px;color:var(--fg);margin-top:1px}
.theme-btn{margin-left:auto;width:34px;height:34px;border:0.5px solid var(--border2);border-radius:50%;background:var(--bg2);color:var(--fg);cursor:pointer;font-size:15px;display:flex;align-items:center;justify-content:center;transition:background .15s;flex-shrink:0}
.theme-btn:hover{background:var(--bg3)}

.result-arrival{font-size:20px;font-weight:600;color:var(--fg);line-height:1.3}
.result-label{font-size:11px;color:var(--fg);text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}
.hint{font-size:11px;color:var(--fg)}
.footer{font-size:11px;color:var(--fg);text-align:right;margin-top:8px}
.pl-10{padding-left:46px}

.timeline{display:flex;flex-direction:column;gap:0}
.tl-row{display:flex;align-items:stretch;gap:0}
.tl-dot-col{display:flex;flex-direction:column;align-items:center;width:28px;flex-shrink:0}
.tl-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0;margin-top:3px}
.tl-dot.drive{background:var(--fg)}
.tl-dot.break{background:#f59e0b}
.tl-dot.rest{background:#6366f1}
.tl-line{width:1.5px;flex:1;min-height:6px;background:var(--border2)}
.tl-body{padding:0 0 14px 10px;flex:1}
.tl-label{font-size:13px;font-weight:500;color:var(--fg)}
.tl-sub{font-size:11px;color:var(--fg);margin-top:1px}
.tl-tag{display:inline-flex;align-items:center;padding:1px 8px;border-radius:100px;font-size:11px;font-weight:500;margin-left:6px}
.tl-tag.drive{background:var(--bg3);color:var(--fg)}
.tl-tag.break{background:#fef3c7;color:#92400e}
.tl-tag.rest{background:#ede9fe;color:#4c1d95}
.dark .tl-tag.break{background:#451a03;color:#fcd34d}
.dark .tl-tag.rest{background:#2e1065;color:#c4b5fd}
.legend-row{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:10px}
.legend-item{display:flex;align-items:center;gap:5px;font-size:11px;color:var(--fg)}
.legend-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0}
</style>
</head>
<body>
<div id="root"></div>
<script type="text/babel">
const { useState, useMemo, useEffect, useCallback } = React;

const TIMEZONES = [
  { label: "CET — Берлин/Варшава/Прага",   tz: "Europe/Berlin" },
  { label: "EET — Киев/Рига/Бухарест",      tz: "Europe/Kiev" },
  { label: "MSK — Москва",                  tz: "Europe/Moscow" },
  { label: "GMT — Лондон",                  tz: "Europe/London" },
  { label: "UTC",                            tz: "UTC" },
  { label: "TRT — Стамбул",                 tz: "Europe/Istanbul" },
  { label: "CEST — Амстердам/Рим/Мадрид",   tz: "Europe/Amsterdam" },
  { label: "FET — Минск",                   tz: "Europe/Minsk" },
];

const TR = {
  ru: {
    appTitle: "Калькулятор рейса", appSub: "Логистика",
    departure: "Время выезда", now: "Сейчас",
    depDate: "Дата выезда", depTime: "Время выезда",
    routeParams: "Параметры рейса", dist: "Расстояние (км)", speed: "Скорость",
    mode: "Режим вождения", single: "Одиночка", crew: "Экипаж",
    alreadyDriven: "Уже проехал сегодня", max: "макс",
    extras: "Дополнительно", fixTime: "Фикс время выгрузки",
    fixDate: "Дата FIX", fixTimeLabel: "Время FIX",
    stops: "Остановки", gas: "Заправка", trailer: "Перецеп", loading: "Загрузка",
    ferry: "Паром", ferryNo: "Нет", ferryH1: "1 час", ferryH2: "2 часа",
    other: "Другое (ч)",
    result: "Результат", arrival: "Расчётное прибытие",
    reserve: "Запас", late: "Опоздание",
    pureDrive: "Чистое время езды", totalTime: "Итоговое время",
    addons: "Допы", remaining: "Остаток вождения", restBlocks: "Использовано девяток",
    scheduleTitle: "Режим труда и отдыха",
    legDrive: "Езда", legBreak: "Перерыв 45 мин", legRest: "Отдых 9 ч",
    breakCalc: "= 1 ч в расчёте",
    reportLine: "Строка для отчёта", copy: "Копировать", copied: "✓ Скопировано",
    orType: "или введи:", hours: "Часы", mins: "Мин", h: "ч",
    plusH1: "+1ч", plusH2: "+2ч", kmh: "км/ч", restH: "9 ч",
    author: "Разработано Aerra AI для Kreiss при помощи Yaroslav Makarovskii",
  },
  en: {
    appTitle: "Trip Calculator", appSub: "Logistics",
    departure: "Departure time", now: "Now",
    depDate: "Departure date", depTime: "Departure time",
    routeParams: "Route parameters", dist: "Distance (km)", speed: "Speed",
    mode: "Driving mode", single: "Solo", crew: "Crew",
    alreadyDriven: "Already driven today", max: "max",
    extras: "Extras", fixTime: "Fixed unload time",
    fixDate: "FIX date", fixTimeLabel: "FIX time",
    stops: "Stops", gas: "Refuel", trailer: "Swap trailer", loading: "Loading",
    ferry: "Ferry", ferryNo: "None", ferryH1: "1 hour", ferryH2: "2 hours",
    other: "Other (h)",
    result: "Result", arrival: "Estimated arrival",
    reserve: "Buffer", late: "Delay",
    pureDrive: "Pure drive time", totalTime: "Total time",
    addons: "Extras", remaining: "Drive remaining", restBlocks: "Rest blocks used",
    scheduleTitle: "Work & rest schedule",
    legDrive: "Drive", legBreak: "Break 45 min", legRest: "Rest 9 h",
    breakCalc: "= 1 h in calc",
    reportLine: "Report line", copy: "Copy", copied: "✓ Copied",
    orType: "or type:", hours: "Hours", mins: "Min", h: "h",
    plusH1: "+1h", plusH2: "+2h", kmh: "km/h", restH: "9 h",
    author: "Developed by Aerra AI for Kreiss with Yaroslav Makarovskii",
  },
  lv: {
    appTitle: "Brauciena kalkulators", appSub: "Loģistika",
    departure: "Izbraukšanas laiks", now: "Tagad",
    depDate: "Izbraukšanas datums", depTime: "Izbraukšanas laiks",
    routeParams: "Maršruta parametri", dist: "Attālums (km)", speed: "Ātrums",
    mode: "Braukšanas režīms", single: "Viens", crew: "Komanda",
    alreadyDriven: "Jau braukts šodien", max: "maks",
    extras: "Papildus", fixTime: "Fiksēts izkraušanas laiks",
    fixDate: "FIX datums", fixTimeLabel: "FIX laiks",
    stops: "Pieturas", gas: "Degviela", trailer: "Piekabe", loading: "Iekraušana",
    ferry: "Prāmis", ferryNo: "Nē", ferryH1: "1 stunda", ferryH2: "2 stundas",
    other: "Cits (h)",
    result: "Rezultāts", arrival: "Paredzamais ierašanās laiks",
    reserve: "Rezerve", late: "Kavēšanās",
    pureDrive: "Tīrais braukšanas laiks", totalTime: "Kopējais laiks",
    addons: "Papildus", remaining: "Atlikušais braukšanas laiks", restBlocks: "Izmantotās devītnieces",
    scheduleTitle: "Darba un atpūtas režīms",
    legDrive: "Braukšana", legBreak: "Pārtraukums 45 min", legRest: "Atpūta 9 h",
    breakCalc: "= 1 h aprēķinā",
    reportLine: "Atskaites rinda", copy: "Kopēt", copied: "✓ Nokopēts",
    orType: "vai ievadi:", hours: "Stundas", mins: "Min", h: "h",
    plusH1: "+1h", plusH2: "+2h", kmh: "km/h", restH: "9 h",
    author: "Izstrādāts Aerra AI priekš Kreiss ar Yaroslav Makarovskii palīdzību",
  },
};

function getNowInTZ(tz) {
  return new Date(new Date().toLocaleString("en-US", { timeZone: tz }));
}
function pad(n) { return String(n).padStart(2, "0"); }

function todayISO(tz) {
  const d = getNowInTZ(tz);
  return `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}`;
}
function tomorrowISO(tz) {
  const d = getNowInTZ(tz); d.setDate(d.getDate()+1);
  return `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}`;
}

const LANG_LOCALE = { ru: "ru-RU", en: "en-GB", lv: "lv-LV" };

function localeDateRu(date, tz, lang) {
  const locale = LANG_LOCALE[lang] || "ru-RU";
  return date.toLocaleString(locale, {
    timeZone: tz, weekday: "long",
    day: "2-digit", month: "2-digit", hour: "2-digit", minute: "2-digit", hour12: false,
  });
}

function buildSchedule({ alreadyDriven, pureDrive, mode }) {
  const steps = [];
  if (mode === "single") {
    const currentLeft = Math.max(0, 9.0 - alreadyDriven);
    if (pureDrive <= currentLeft) {
      if (alreadyDriven < 4.5 && alreadyDriven + pureDrive > 4.5) {
        const d1 = 4.5 - alreadyDriven;
        steps.push({ type:"drive", hours: d1 });
        steps.push({ type:"break", hours: 1 });
        steps.push({ type:"drive", hours: pureDrive - d1 });
      } else {
        steps.push({ type:"drive", hours: pureDrive });
      }
    } else {
      // first partial day
      if (alreadyDriven < 4.5) {
        const d1 = 4.5 - alreadyDriven;
        const d2 = currentLeft - d1;
        steps.push({ type:"drive", hours: d1 });
        steps.push({ type:"break", hours: 1 });
        if (d2 > 0) steps.push({ type:"drive", hours: d2 });
      } else {
        if (currentLeft > 0) steps.push({ type:"drive", hours: currentLeft });
      }
      steps.push({ type:"rest", hours: 9 });
      let rem = pureDrive - currentLeft;
      while (rem > 0) {
        const block = Math.min(9, rem);
        if (block > 4.5) {
          steps.push({ type:"drive", hours: 4.5 });
          steps.push({ type:"break", hours: 1 });
          steps.push({ type:"drive", hours: block - 4.5 });
          steps.push({ type:"break", hours: 1 });
        } else if (block === 4.5) {
          steps.push({ type:"drive", hours: 4.5 });
          steps.push({ type:"break", hours: 1 });
        } else {
          steps.push({ type:"drive", hours: block });
          if (rem - block <= 0) {/* last block, no forced break */} else {
            steps.push({ type:"break", hours: 1 });
          }
        }
        rem -= block;
        if (rem > 0) steps.push({ type:"rest", hours: 9 });
      }
    }
  } else {
    const currentLeft = Math.max(0, 18.0 - alreadyDriven);
    if (pureDrive <= currentLeft) {
      steps.push({ type:"drive", hours: pureDrive });
    } else {
      if (currentLeft > 0) steps.push({ type:"drive", hours: currentLeft });
      steps.push({ type:"rest", hours: 9 });
      let rem = pureDrive - currentLeft;
      while (rem > 0) {
        const block = Math.min(18, rem);
        steps.push({ type:"drive", hours: block });
        rem -= block;
        if (rem > 0) steps.push({ type:"rest", hours: 9 });
      }
    }
  }
  return steps;
}

function calcArrival({ useCurrent, startDate, startHour, startMin, tz, dist, speed, mode, alreadyDriven, gas, trailer, loading, ferry, misc }) {
  let startDt;
  if (useCurrent) {
    startDt = new Date();
  } else {
    const naive = new Date(`${startDate}T${pad(startHour)}:${pad(startMin)}:00`);
    const tzNow = new Date(naive.toLocaleString("en-US", { timeZone: tz }));
    const offsetMs = naive - tzNow;
    startDt = new Date(naive.getTime() + offsetMs);
  }

  const extra = (gas?1:0)+(trailer?1:0)+(loading?2:0)+Number(misc)+Number(ferry);
  const pureDrive = dist / speed;
  const limit = mode === "single" ? 9.0 : 18.0;
  const currentLeft = Math.max(0, limit - alreadyDriven);
  let totalWay, driveRemaining, restBlocks, breaks45;

  if (mode === "single") {
    if (pureDrive <= currentLeft) {
      const needBreak = alreadyDriven < 4.5 && alreadyDriven+pureDrive > 4.5 ? 1 : 0;
      totalWay = pureDrive + needBreak;
      driveRemaining = currentLeft - pureDrive;
      restBlocks = 0;
      breaks45 = needBreak;
    } else {
      const rem = pureDrive - currentLeft;
      const shifts = Math.ceil(rem / 9);
      totalWay = pureDrive + shifts*9 + (alreadyDriven<4.5?1:0) + shifts*2;
      driveRemaining = rem%9 !== 0 ? 9-(rem%9) : 9;
      restBlocks = shifts;
      breaks45 = (alreadyDriven<4.5?1:0) + shifts*2;
    }
  } else {
    const shifts = pureDrive > currentLeft ? Math.ceil((pureDrive-currentLeft)/18) : 0;
    totalWay = pureDrive + shifts*9;
    driveRemaining = shifts===0 ? currentLeft-pureDrive : 18-((pureDrive-currentLeft)%18);
    restBlocks = shifts;
    breaks45 = 0;
  }

  const schedule = buildSchedule({ alreadyDriven, pureDrive, mode });

  totalWay += extra;
  const arrival = new Date(startDt.getTime() + totalWay*3600000);
  const cetNow = getNowInTZ("Europe/Berlin");
  const checkVal = cetNow.getHours() < 12 ? "1/2" : "2/2";
  const a = new Date(arrival.toLocaleString("en-US", { timeZone: "Europe/Berlin" }));
  const workString = `${checkVal} ETA ${pad(a.getDate())}.${pad(a.getMonth()+1)} ${pad(a.getHours())}:${pad(a.getMinutes())}CET D/H ${driveRemaining.toFixed(1)}`;
  return { arrival, workString, driveRemaining, pureDrive: pureDrive.toFixed(1), totalWay: totalWay.toFixed(1), extra, restBlocks, breaks45, schedule };
}

function SwitchEl({ id, checked, onChange }) {
  return (
    <label className="switch">
      <input type="checkbox" id={id} checked={checked} onChange={e => onChange(e.target.checked)} />
      <span className="switch-track"></span>
    </label>
  );
}

function TimeSliderPicker({ hour, minute, onHourChange, onMinuteChange, t }) {
  t = t || TR.ru;
  const [rawInput, setRawInput] = useState(`${pad(hour)}:${pad(minute)}`);
  const [inputFocused, setInputFocused] = useState(false);

  useEffect(() => {
    if (!inputFocused) setRawInput(`${pad(hour)}:${pad(minute)}`);
  }, [hour, minute, inputFocused]);

  function handleInputChange(e) {
    const v = e.target.value;
    setRawInput(v);
    const m = v.match(/^(\d{1,2}):(\d{2})$/);
    if (m) {
      const h = Math.min(23, parseInt(m[1]));
      const min = Math.min(59, parseInt(m[2]));
      onHourChange(h);
      onMinuteChange(min);
    }
  }

  function handleInputBlur() {
    setInputFocused(false);
    setRawInput(`${pad(hour)}:${pad(minute)}`);
  }

  return (
    <div className="time-slider-block">
      <div className="time-display">{pad(hour)}:{pad(minute)}</div>
      <div className="slider-row">
        <span className="slider-lbl">{t.hours}</span>
        <input type="range" min="0" max="23" value={hour}
          onChange={e => { onHourChange(Number(e.target.value)); }} style={{flex:1}} />
        <span className="slider-val">{pad(hour)}</span>
      </div>
      <div className="slider-row">
        <span className="slider-lbl">{t.mins}</span>
        <input type="range" min="0" max="59" value={minute}
          onChange={e => { onMinuteChange(Number(e.target.value)); }} style={{flex:1}} />
        <span className="slider-val">{pad(minute)}</span>
      </div>
      <div className="time-input-row">
        <span>{t.orType}</span>
        <input type="text" value={rawInput} placeholder="14:30" style={{width:90}}
          onFocus={() => setInputFocused(true)}
          onChange={handleInputChange}
          onBlur={handleInputBlur} />
      </div>
    </div>
  );
}

function App() {
  const [tz, setTz] = useState("Europe/Berlin");
  const now = getNowInTZ(tz);

  const [dark, setDark] = useState(() => window.matchMedia("(prefers-color-scheme: dark)").matches);
  const [useCurrent, setUseCurrent] = useState(true);
  const [startDate, setStartDate] = useState(() => todayISO("Europe/Berlin"));
  const [startHour, setStartHour] = useState(() => getNowInTZ("Europe/Berlin").getHours());
  const [startMin, setStartMin] = useState(() => getNowInTZ("Europe/Berlin").getMinutes());

  const [dist, setDist] = useState(1000);
  const [speed, setSpeed] = useState(70);
  const [mode, setMode] = useState("single");
  const [alreadyDriven, setAlreadyDriven] = useState(0);

  const [useFix, setUseFix] = useState(false);
  const [fixDate, setFixDate] = useState(() => tomorrowISO("Europe/Berlin"));
  const [fixHour, setFixHour] = useState(8);
  const [fixMin, setFixMin] = useState(0);

  const [gas, setGas] = useState(false);
  const [trailer, setTrailer] = useState(false);
  const [loading, setLoading] = useState(false);
  const [ferry, setFerry] = useState("0");
  const [misc, setMisc] = useState("0");
  const [copied, setCopied] = useState(false);
  const [lang, setLang] = useState("ru");
  const t = TR[lang];

  useEffect(() => {
    document.documentElement.className = dark ? "dark" : "";
  }, [dark]);

  // When tz changes, update "now" display
  useEffect(() => {
    if (useCurrent) {
      const n = getNowInTZ(tz);
      setStartHour(n.getHours());
      setStartMin(n.getMinutes());
      setStartDate(todayISO(tz));
    }
  }, [tz]);

  const maxDrive = mode === "single" ? 9 : 18;
  const tzLabel = TIMEZONES.find(t => t.tz === tz)?.label.split("—")[0].trim() || tz;

  const result = useMemo(() => calcArrival({
    useCurrent, startDate, startHour, startMin, tz,
    dist, speed, mode, alreadyDriven,
    gas, trailer, loading, ferry, misc,
  }), [useCurrent, startDate, startHour, startMin, tz, dist, speed, mode, alreadyDriven, gas, trailer, loading, ferry, misc]);

  const arrivalLabel = useMemo(() => { const s = localeDateRu(result.arrival, tz, lang) + " " + tzLabel; return s.charAt(0).toUpperCase() + s.slice(1); }, [result.arrival, tz, lang]);

  const fixDiff = useMemo(() => {
    if (!useFix) return null;
    const naive = new Date(`${fixDate}T${pad(fixHour)}:${pad(fixMin)}:00`);
    const tzNow = new Date(naive.toLocaleString("en-US", { timeZone: tz }));
    const offsetMs = naive - tzNow;
    const fixDt = new Date(naive.getTime() + offsetMs);
    return (fixDt.getTime() - result.arrival.getTime()) / 3600000;
  }, [useFix, fixDate, fixHour, fixMin, tz, result.arrival]);

  const fixH = fixDiff !== null ? Math.floor(Math.abs(fixDiff)) : 0;
  const fixM = fixDiff !== null ? Math.round((Math.abs(fixDiff)%1)*60) : 0;
  const fixOk = fixDiff !== null && fixDiff >= 0;

  function copy() {
    try {
      const ta = document.createElement("textarea");
      ta.value = result.workString;
      ta.style.position = "fixed"; ta.style.opacity = "0";
      document.body.appendChild(ta); ta.focus(); ta.select();
      document.execCommand("copy");
      document.body.removeChild(ta);
      setCopied(true); setTimeout(() => setCopied(false), 1500);
    } catch(e) {}
  }

  return (
    <div className="app">
      {/* Header */}
      <div className="header">
        <div className="header-icon">🚛</div>
        <div>
          <div className="header-title">{t.appTitle}</div>
          <div className="header-sub flex-row" style={{gap:6}}>
            {t.appSub} · <span className="tz-badge">{tzLabel}</span>
          </div>
        </div>
        <div style={{marginLeft:"auto", display:"flex", alignItems:"center", gap:10}}>
          <div style={{display:"flex", gap:3}}>
            {["ru","en","lv"].map(l => (
              <button key={l} onClick={() => setLang(l)}
                style={{height:28, padding:"0 8px", border:"0.5px solid var(--border2)", borderRadius:"var(--radius)",
                  background: lang===l ? "var(--primary)" : "var(--bg2)",
                  color: lang===l ? "var(--primary-fg)" : "var(--fg)",
                  fontFamily:"inherit", fontSize:11, fontWeight:600, cursor:"pointer", textTransform:"uppercase"}}>
                {l}
              </button>
            ))}
          </div>
          <select value={tz} onChange={e => setTz(e.target.value)}
            style={{height:30, fontSize:12, padding:"0 8px", background:"var(--bg2)", border:"0.5px solid var(--border2)", borderRadius:"var(--radius)", color:"var(--fg)", fontFamily:"inherit", outline:"none", maxWidth:200}}>
            {TIMEZONES.map(zone => <option key={zone.tz} value={zone.tz}>{zone.label}</option>)}
          </select>
          <button className="theme-btn" onClick={() => setDark(d => !d)}>{dark ? "☀️" : "🌙"}</button>
        </div>
      </div>

      <div className="main-layout">
        {/* LEFT — одна большая карточка */}
        <div className="left-col">
          <div className="combined-card">

            {/* Время выезда */}
            <div className="card-title">{t.departure}</div>
            <div className="switch-row" style={{marginBottom: useCurrent ? 0 : 14}}>
              <SwitchEl id="use-current" checked={useCurrent} onChange={setUseCurrent} />
              <label htmlFor="use-current" style={{cursor:"pointer", fontSize:13}}>
                {t.now} — <span style={{color:"var(--fg2)"}}>{pad(now.getHours())}:{pad(now.getMinutes())} · {pad(now.getDate())}.{pad(now.getMonth()+1)} ({tzLabel})</span>
              </label>
            </div>
            {!useCurrent && (
              <div className="space-y mt-8">
                <div>
                  <label className="field-label">{t.depDate}</label>
                  <input type="date" value={startDate} onChange={e => setStartDate(e.target.value)} />
                </div>
                <div>
                  <label className="field-label">{t.depTime}</label>
                  <TimeSliderPicker
                    hour={startHour} minute={startMin}
                    onHourChange={setStartHour} onMinuteChange={setStartMin}
                    lang={lang} t={t}
                  />
                </div>
              </div>
            )}

            <div className="section-sep"></div>

            {/* Параметры рейса */}
            <div className="card-title">{t.routeParams}</div>
            <div className="space-y">
              <div>
                <label className="field-label">{t.dist}</label>
                <input type="number" min="1" max="5000" value={dist} onChange={e => setDist(Math.min(5000, Number(e.target.value)))} />
              </div>
              <div>
                <div className="flex-bw" style={{marginBottom:6}}>
                  <label className="field-label" style={{margin:0}}>{t.speed}</label>
                  <span style={{fontSize:13, fontWeight:500}}>{speed} {t.kmh}</span>
                </div>
                <input type="range" min="40" max="90" value={speed} onChange={e => setSpeed(Number(e.target.value))} />
                <div className="flex-bw mt-4"><span className="hint">40</span><span className="hint">90</span></div>
              </div>
              <div>
                <label className="field-label">{t.mode}</label>
                <div className="radio-group">
                  <div className={`radio-btn ${mode==="single"?"active":""}`} onClick={() => setMode("single")}>{t.single}</div>
                  <div className={`radio-btn ${mode==="crew"?"active":""}`} onClick={() => setMode("crew")}>{t.crew}</div>
                </div>
              </div>
              <div>
                <div className="flex-bw" style={{marginBottom:5}}>
                  <label className="field-label" style={{margin:0}}>{t.alreadyDriven}</label>
                  <span className="hint">{t.max} {maxDrive}ч</span>
                </div>
                <input type="number" min="0" max={maxDrive} step="0.5" value={alreadyDriven}
                  onChange={e => setAlreadyDriven(Math.min(maxDrive, Number(e.target.value)))} />
              </div>
            </div>

            <div className="section-sep"></div>

            {/* Дополнительно */}
            <div className="card-title">{t.extras}</div>
            <div className="space-y">
              <div>
                <div className="switch-row">
                  <SwitchEl id="use-fix" checked={useFix} onChange={setUseFix} />
                  <label htmlFor="use-fix" style={{cursor:"pointer", fontSize:13}}>{t.fixTime}</label>
                </div>
                {useFix && (
                  <div className="pl-10 mt-8 space-y">
                    <div>
                      <label className="field-label">{t.fixDate}</label>
                      <input type="date" value={fixDate} onChange={e => setFixDate(e.target.value)} />
                    </div>
                    <div>
                      <label className="field-label">{t.fixTimeLabel}</label>
                      <TimeSliderPicker
                        hour={fixHour} minute={fixMin}
                        onHourChange={setFixHour} onMinuteChange={setFixMin}
                        lang={lang} t={t}
                      />
                    </div>
                  </div>
                )}
              </div>
              <div className="sep"></div>
              <div className="space-y-sm">
                <div style={{fontSize:11, textTransform:"uppercase", letterSpacing:"0.07em"}}>{t.stops}</div>
                {[
                  {id:"gas",   label:t.gas,     plus:t.plusH1, val:gas,     set:setGas},
                  {id:"trail", label:t.trailer,  plus:t.plusH1, val:trailer, set:setTrailer},
                  {id:"load",  label:t.loading,  plus:t.plusH2, val:loading, set:setLoading},
                ].map(({id,label,plus,val,set}) => (
                  <div key={id} className="switch-row">
                    <SwitchEl id={id} checked={val} onChange={set} />
                    <label htmlFor={id} style={{cursor:"pointer", fontSize:13, display:"flex", gap:6, alignItems:"center"}}>
                      {label} <span className="badge">{plus}</span>
                    </label>
                  </div>
                ))}
              </div>
              <div className="grid2">
                <div>
                  <label className="field-label">{t.ferry}</label>
                  <select value={ferry} onChange={e => setFerry(e.target.value)}>
                    <option value="0">{t.ferryNo}</option><option value="1">{t.ferryH1}</option><option value="2">{t.ferryH2}</option>
                  </select>
                </div>
                <div>
                  <label className="field-label">{t.other}</label>
                  <select value={misc} onChange={e => setMisc(e.target.value)}>
                    {[0,1,2,3,4,5].map(v => <option key={v} value={v}>{v}</option>)}
                  </select>
                </div>
              </div>
            </div>

          </div>
        </div>

        {/* RIGHT — Результат */}
        <div className="right-col">
          <div className="card">
            <div className="card-title">{t.result}</div>
            <div className="grid2" style={{gap:20, alignItems:"start"}}>
              <div>
                <div className="result-label">{t.arrival}</div>
                <div className="result-arrival">{arrivalLabel}</div>
                {useFix && fixDiff !== null && (
                  <div className={`alert mt-12 ${fixOk?"alert-success":"alert-danger"}`}>
                    <span>{fixOk ? "✓" : "✗"}</span>
                    <span>{fixOk ? `${t.reserve}: ${fixH}ч ${fixM}м` : `${t.late}: ${fixH}ч ${fixM}м`}</span>
                  </div>
                )}
              </div>
              <div>
                {[
                  [t.pureDrive,   `${result.pureDrive} ${t.h}`],
                  [t.totalTime,   `${result.totalWay} ${t.h}`],
                  [t.addons,      `${result.extra} ${t.h}`],
                  [t.remaining,   `${Math.floor(result.driveRemaining)} ${t.h}`],
                  [t.restBlocks,  `${result.restBlocks}`],
                ].map(([l, v]) => (
                  <div key={l} className="stat-row">
                    <span className="stat-label">{l}</span>
                    <span className="stat-value">{v}</span>
                  </div>
                ))}
              </div>
            </div>
            <div className="sep mt-12" style={{marginBottom:12}}></div>
            <div className="result-label">{t.scheduleTitle}</div>
            <div className="legend-row">
              <span className="legend-item"><span className="legend-dot" style={{background:"var(--fg)"}}></span>{t.legDrive}</span>
              <span className="legend-item"><span className="legend-dot" style={{background:"#f59e0b"}}></span>{t.legBreak}</span>
              <span className="legend-item"><span className="legend-dot" style={{background:"#6366f1"}}></span>{t.legRest}</span>
            </div>
            <div className="timeline">
              {result.schedule.map((step, i) => {
                const isLast = i === result.schedule.length - 1;
                const labels = { drive: t.legDrive, break: t.legBreak, rest: t.legRest };
                const subs = {
                  drive: `${step.hours.toFixed(1)} ${t.h}`,
                  break: t.breakCalc,
                  rest: t.restH,
                };
                return (
                  <div key={i} className="tl-row">
                    <div className="tl-dot-col">
                      <div className={`tl-dot ${step.type}`}></div>
                      {!isLast && <div className="tl-line"></div>}
                    </div>
                    <div className="tl-body">
                      <span className="tl-label">{labels[step.type]}</span>
                      <span className={`tl-tag ${step.type}`}>{subs[step.type]}</span>
                    </div>
                  </div>
                );
              })}
            </div>
            <div className="sep mt-12" style={{marginBottom:12}}></div>
            <div className="result-label">{t.reportLine}</div>
            <div className="code-row">
              <code>{result.workString}</code>
              <button className="copy-btn" onClick={copy}>{copied ? t.copied : t.copy}</button>
            </div>
          </div>
        </div>
      </div>

      </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
</script>
</body>
</html>
"""

components.html(HTML, height=950, scrolling=True)
