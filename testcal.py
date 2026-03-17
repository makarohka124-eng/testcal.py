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
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg: #ffffff; --bg2: #f4f4f5; --bg3: #e4e4e7;
    --fg: #09090b; --fg2: #52525b;
    --border: rgba(0,0,0,0.12); --border2: rgba(0,0,0,0.22);
    --radius: 8px; --radius-lg: 12px;
    --card-bg: #ffffff; --muted-bg: #f4f4f5;
    --success-bg: #f0fdf4; --success-fg: #166534; --success-border: #bbf7d0;
    --danger-bg: #fef2f2; --danger-fg: #991b1b; --danger-border: #fecaca;
    --badge-bg: #e4e4e7; --badge-fg: #3f3f46;
    --primary: #09090b; --primary-fg: #fafafa;
  }
  .dark {
    --bg: #09090b; --bg2: #18181b; --bg3: #27272a;
    --fg: #fafafa; --fg2: #a1a1aa;
    --border: rgba(255,255,255,0.1); --border2: rgba(255,255,255,0.18);
    --card-bg: #18181b; --muted-bg: #27272a;
    --success-bg: #052e16; --success-fg: #86efac; --success-border: #166534;
    --danger-bg: #450a0a; --danger-fg: #fca5a5; --danger-border: #991b1b;
    --badge-bg: #3f3f46; --badge-fg: #d4d4d8;
    --primary: #fafafa; --primary-fg: #09090b;
  }

  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: var(--bg); color: var(--fg); font-size: 14px; transition: background 0.2s, color 0.2s; }
  .app { max-width: 720px; margin: 0 auto; padding: 24px 16px 48px; }

  .card { background: var(--card-bg); border: 0.5px solid var(--border); border-radius: var(--radius-lg); padding: 16px 20px; transition: background 0.2s, border-color 0.2s; }
  .card-title { font-size: 11px; font-weight: 500; color: var(--fg); letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 14px; }

  .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
  .flex-row { display: flex; align-items: center; gap: 8px; }
  .flex-between { display: flex; align-items: center; justify-content: space-between; }
  .space-y > * + * { margin-top: 14px; }
  .space-y-sm > * + * { margin-top: 8px; }
  .mt-4 { margin-top: 4px; } .mt-8 { margin-top: 8px; } .mt-12 { margin-top: 12px; } .mt-16 { margin-top: 16px; }

  label.field-label { display: block; font-size: 12px; color: var(--fg); margin-bottom: 5px; }
  input[type="number"], input[type="date"], input[type="time"], select {
    width: 100%; height: 34px; padding: 0 10px;
    background: var(--bg2); border: 0.5px solid var(--border2);
    border-radius: var(--radius); color: var(--fg); font-size: 13px;
    font-family: inherit; outline: none; transition: border-color 0.15s, box-shadow 0.15s;
  }
  input:focus, select:focus { border-color: var(--fg2); box-shadow: 0 0 0 2px rgba(128,128,128,0.15); }
  input[type="range"] { width: 100%; accent-color: var(--fg); height: 4px; cursor: pointer; }

  .switch { position: relative; width: 36px; height: 20px; flex-shrink: 0; }
  .switch input { opacity: 0; width: 0; height: 0; }
  .switch-track { position: absolute; inset: 0; background: var(--border2); border-radius: 100px; transition: background 0.2s; cursor: pointer; }
  .switch input:checked + .switch-track { background: var(--primary); }
  .switch-track::after { content: ''; position: absolute; width: 14px; height: 14px; left: 3px; top: 3px; background: white; border-radius: 50%; transition: transform 0.2s; }
  .switch input:checked + .switch-track::after { transform: translateX(16px); }
  .switch-row { display: flex; align-items: center; gap: 10px; cursor: pointer; user-select: none; }

  .radio-group { display: flex; gap: 8px; }
  .radio-btn { flex: 1; height: 34px; display: flex; align-items: center; justify-content: center; border: 0.5px solid var(--border2); border-radius: var(--radius); font-size: 13px; cursor: pointer; background: var(--bg2); color: var(--fg); transition: all 0.15s; user-select: none; }
  .radio-btn.active { background: var(--primary); color: var(--primary-fg); border-color: var(--primary); }

  .badge { display: inline-flex; align-items: center; padding: 1px 7px; border-radius: 100px; font-size: 11px; font-weight: 500; background: var(--badge-bg); color: var(--badge-fg); }
  .sep { height: 0.5px; background: var(--border); margin: 4px 0; }

  .alert { padding: 10px 12px; border-radius: var(--radius); border: 0.5px solid; font-size: 13px; display: flex; align-items: center; gap: 8px; }
  .alert-success { background: var(--success-bg); border-color: var(--success-border); color: var(--success-fg); }
  .alert-danger  { background: var(--danger-bg);  border-color: var(--danger-border);  color: var(--danger-fg); }

  .stat-row { display: flex; justify-content: space-between; align-items: center; padding: 6px 0; border-bottom: 0.5px solid var(--border); }
  .stat-row:last-child { border-bottom: none; }
  .stat-label { font-size: 12px; color: var(--fg); }
  .stat-value { font-size: 13px; font-weight: 500; color: var(--fg); }

  .code-row { display: flex; align-items: center; gap: 10px; background: var(--muted-bg); border-radius: var(--radius); padding: 10px 12px; }
  .code-row code { flex: 1; font-family: monospace; font-size: 13px; color: var(--fg); }
  .copy-btn { height: 28px; padding: 0 10px; flex-shrink: 0; border: 0.5px solid var(--border2); border-radius: var(--radius); background: var(--bg); color: var(--fg); font-size: 12px; cursor: pointer; font-family: inherit; transition: background 0.1s; }
  .copy-btn:hover { background: var(--bg3); }

  .header { display: flex; align-items: center; gap: 12px; margin-bottom: 20px; }
  .header-icon { width: 36px; height: 36px; border-radius: var(--radius); background: var(--primary); display: flex; align-items: center; justify-content: center; font-size: 18px; flex-shrink: 0; }
  .header-title { font-size: 18px; font-weight: 600; color: var(--fg); }
  .header-sub { font-size: 12px; color: var(--fg); margin-top: 1px; }
  .theme-btn { margin-left: auto; width: 34px; height: 34px; border: 0.5px solid var(--border2); border-radius: 50%; background: var(--bg2); color: var(--fg); cursor: pointer; font-size: 15px; display: flex; align-items: center; justify-content: center; transition: background 0.15s; flex-shrink: 0; }
  .theme-btn:hover { background: var(--bg3); }

  .result-arrival { font-size: 20px; font-weight: 600; color: var(--fg); line-height: 1.3; }
  .result-label { font-size: 11px; color: var(--fg); text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 4px; }
  .hint { font-size: 11px; color: var(--fg); }
  .footer { font-size: 11px; color: var(--fg); text-align: right; margin-top: 8px; }
  .pl-10 { padding-left: 46px; }
</style>
</head>
<body>
<div id="root"></div>
<script type="text/babel">
const { useState, useMemo, useEffect } = React;

function getCETNow() {
  return new Date(new Date().toLocaleString("en-US", { timeZone: "Europe/Berlin" }));
}
function pad(n) { return String(n).padStart(2, "0"); }
function todayISO() {
  const d = getCETNow();
  return `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}`;
}
function tomorrowISO() {
  const d = getCETNow(); d.setDate(d.getDate()+1);
  return `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}`;
}
function nowTimeStr() {
  const d = getCETNow();
  return `${pad(d.getHours())}:${pad(d.getMinutes())}`;
}
function localeDateRu(date) {
  return date.toLocaleString("ru-RU", {
    timeZone: "Europe/Berlin", weekday: "long",
    day: "2-digit", month: "2-digit", hour: "2-digit", minute: "2-digit", hour12: false,
  });
}

function calcArrival({ useCurrent, startDate, startTime, dist, speed, mode, alreadyDriven, gas, trailer, loading, ferry, misc }) {
  const startDt = useCurrent ? getCETNow() : new Date(`${startDate}T${startTime}:00`);
  const extra = (gas?1:0)+(trailer?1:0)+(loading?2:0)+Number(misc)+Number(ferry);
  const pureDrive = dist / speed;
  const limit = mode === "single" ? 9.0 : 18.0;
  const currentLeft = Math.max(0, limit - alreadyDriven);
  let totalWay, driveRemaining;
  if (mode === "single") {
    if (pureDrive <= currentLeft) {
      const needBreak = alreadyDriven < 4.5 && alreadyDriven+pureDrive > 4.5 ? 1 : 0;
      totalWay = pureDrive + needBreak;
      driveRemaining = currentLeft - pureDrive;
    } else {
      const rem = pureDrive - currentLeft;
      const shifts = Math.ceil(rem / 9);
      totalWay = pureDrive + shifts*9 + (alreadyDriven<4.5?1:0) + shifts*2;
      driveRemaining = rem%9 !== 0 ? 9-(rem%9) : 9;
    }
  } else {
    const shifts = pureDrive > currentLeft ? Math.ceil((pureDrive-currentLeft)/18) : 0;
    totalWay = pureDrive + shifts*9;
    driveRemaining = shifts===0 ? currentLeft-pureDrive : 18-((pureDrive-currentLeft)%18);
  }
  totalWay += extra;
  const arrival = new Date(startDt.getTime() + totalWay*3600000);
  const cetNow = getCETNow();
  const checkVal = cetNow.getHours() < 12 ? "1/2" : "2/2";
  const a = new Date(arrival.toLocaleString("en-US", { timeZone: "Europe/Berlin" }));
  const workString = `${checkVal} ETA ${pad(a.getDate())}.${pad(a.getMonth()+1)} ${pad(a.getHours())}:${pad(a.getMinutes())}CET D/H ${Math.floor(driveRemaining)}`;
  return { arrival, workString, driveRemaining, pureDrive: pureDrive.toFixed(1), totalWay: totalWay.toFixed(1), extra };
}

function SwitchEl({ id, checked, onChange }) {
  return (
    <label className="switch">
      <input type="checkbox" id={id} checked={checked} onChange={e => onChange(e.target.checked)} />
      <span className="switch-track"></span>
    </label>
  );
}

function App() {
  const now = getCETNow();
  const [dark, setDark] = useState(() => window.matchMedia("(prefers-color-scheme: dark)").matches);
  const [useCurrent, setUseCurrent] = useState(true);
  const [startDate, setStartDate] = useState(todayISO);
  const [startTime, setStartTime] = useState(nowTimeStr);
  const [dist, setDist] = useState(1000);
  const [speed, setSpeed] = useState(70);
  const [mode, setMode] = useState("single");
  const [alreadyDriven, setAlreadyDriven] = useState(0);
  const [useFix, setUseFix] = useState(false);
  const [fixDate, setFixDate] = useState(tomorrowISO);
  const [fixTime, setFixTime] = useState("08:00");
  const [gas, setGas] = useState(false);
  const [trailer, setTrailer] = useState(false);
  const [loading, setLoading] = useState(false);
  const [ferry, setFerry] = useState("0");
  const [misc, setMisc] = useState("0");
  const [copied, setCopied] = useState(false);

  useEffect(() => {
    document.documentElement.className = dark ? "dark" : "";
  }, [dark]);

  const maxDrive = mode === "single" ? 9 : 18;
  const result = useMemo(() => calcArrival({
    useCurrent, startDate, startTime, dist, speed, mode, alreadyDriven,
    gas, trailer, loading, ferry, misc,
  }), [useCurrent, startDate, startTime, dist, speed, mode, alreadyDriven, gas, trailer, loading, ferry, misc]);

  const arrivalLabel = useMemo(() => localeDateRu(result.arrival), [result.arrival]);

  const fixDiff = useMemo(() => {
    if (!useFix) return null;
    const fixDt = new Date(`${fixDate}T${fixTime}:00`);
    return (fixDt.getTime() - result.arrival.getTime()) / 3600000;
  }, [useFix, fixDate, fixTime, result.arrival]);

  const fixH = fixDiff !== null ? Math.floor(Math.abs(fixDiff)) : 0;
  const fixM = fixDiff !== null ? Math.round((Math.abs(fixDiff)%1)*60) : 0;
  const fixOk = fixDiff !== null && fixDiff >= 0;

  function copy() {
    try {
      const ta = document.createElement("textarea");
      ta.value = result.workString;
      ta.style.position = "fixed";
      ta.style.opacity = "0";
      document.body.appendChild(ta);
      ta.focus();
      ta.select();
      document.execCommand("copy");
      document.body.removeChild(ta);
      setCopied(true);
      setTimeout(() => setCopied(false), 1500);
    } catch(e) {}
  }

  return (
    <div className="app">
      <div className="header">
        <div className="header-icon">🚛</div>
        <div>
          <div className="header-title">Калькулятор рейса</div>
          <div className="header-sub">Логистика · CET</div>
        </div>
        <button className="theme-btn" onClick={() => setDark(d => !d)}>
          {dark ? "☀️" : "🌙"}
        </button>
      </div>

      <div className="card" style={{marginBottom:12}}>
        <div className="card-title">Время выезда</div>
        <div className="switch-row">
          <SwitchEl id="use-current" checked={useCurrent} onChange={setUseCurrent} />
          <label htmlFor="use-current" style={{cursor:"pointer", fontSize:13}}>
            Сейчас — <span style={{color:"var(--fg2)"}}>{pad(now.getHours())}:{pad(now.getMinutes())} · {pad(now.getDate())}.{pad(now.getMonth()+1)}</span>
          </label>
        </div>
        {!useCurrent && (
          <div className="grid2 mt-8">
            <div><label className="field-label">Дата выезда</label><input type="date" value={startDate} onChange={e => setStartDate(e.target.value)} /></div>
            <div><label className="field-label">Время (CET)</label><input type="time" value={startTime} onChange={e => setStartTime(e.target.value)} /></div>
          </div>
        )}
      </div>

      <div className="grid2" style={{marginBottom:12, alignItems:"start"}}>
        <div className="card">
          <div className="card-title">Параметры рейса</div>
          <div className="space-y">
            <div>
              <label className="field-label">Расстояние (км)</label>
              <input type="number" min="1" value={dist} onChange={e => setDist(Number(e.target.value))} />
            </div>
            <div>
              <div className="flex-between" style={{marginBottom:6}}>
                <label className="field-label" style={{margin:0}}>Скорость</label>
                <span style={{fontSize:13, fontWeight:500}}>{speed} км/ч</span>
              </div>
              <input type="range" min="40" max="90" value={speed} onChange={e => setSpeed(Number(e.target.value))} />
              <div className="flex-between mt-4"><span className="hint">40</span><span className="hint">90</span></div>
            </div>
            <div>
              <label className="field-label">Режим вождения</label>
              <div className="radio-group">
                <div className={`radio-btn ${mode==="single"?"active":""}`} onClick={() => setMode("single")}>Одиночка</div>
                <div className={`radio-btn ${mode==="crew"?"active":""}`} onClick={() => setMode("crew")}>Экипаж</div>
              </div>
            </div>
            <div>
              <div className="flex-between" style={{marginBottom:5}}>
                <label className="field-label" style={{margin:0}}>Уже проехал сегодня</label>
                <span className="hint">макс {maxDrive}ч</span>
              </div>
              <input type="number" min="0" max={maxDrive} step="0.5" value={alreadyDriven}
                onChange={e => setAlreadyDriven(Math.min(maxDrive, Number(e.target.value)))} />
            </div>
          </div>
        </div>

        <div className="card">
          <div className="card-title">Дополнительно</div>
          <div className="space-y">
            <div>
              <div className="switch-row">
                <SwitchEl id="use-fix" checked={useFix} onChange={setUseFix} />
                <label htmlFor="use-fix" style={{cursor:"pointer", fontSize:13}}>Фикс время выгрузки</label>
              </div>
              {useFix && (
                <div className="grid2 pl-10 mt-8">
                  <div><label className="field-label">Дата FIX</label><input type="date" value={fixDate} onChange={e => setFixDate(e.target.value)} /></div>
                  <div><label className="field-label">Время FIX</label><input type="time" value={fixTime} onChange={e => setFixTime(e.target.value)} /></div>
                </div>
              )}
            </div>
            <div className="sep"></div>
            <div className="space-y-sm">
              <div style={{fontSize:11, textTransform:"uppercase", letterSpacing:"0.07em"}}>Остановки</div>
              {[
                {id:"gas",   label:"Заправка", plus:"+1ч", val:gas,     set:setGas},
                {id:"trail", label:"Перецеп",  plus:"+1ч", val:trailer, set:setTrailer},
                {id:"load",  label:"Загрузка", plus:"+2ч", val:loading, set:setLoading},
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
                <label className="field-label">Паром</label>
                <select value={ferry} onChange={e => setFerry(e.target.value)}>
                  <option value="0">Нет</option><option value="1">1 час</option><option value="2">2 часа</option>
                </select>
              </div>
              <div>
                <label className="field-label">Другое (ч)</label>
                <select value={misc} onChange={e => setMisc(e.target.value)}>
                  {[0,1,2,3,4,5].map(v => <option key={v} value={v}>{v}</option>)}
                </select>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="card">
        <div className="card-title">Результат</div>
        <div className="grid2" style={{gap:20, alignItems:"start"}}>
          <div>
            <div className="result-label">Расчётное прибытие</div>
            <div className="result-arrival">{arrivalLabel}</div>
            {useFix && fixDiff !== null && (
              <div className={`alert mt-12 ${fixOk?"alert-success":"alert-danger"}`}>
                <span>{fixOk ? "✓" : "✗"}</span>
                <span>{fixOk ? `Запас: ${fixH}ч ${fixM}м` : `Опоздание: ${fixH}ч ${fixM}м`}</span>
              </div>
            )}
          </div>
          <div>
            {[
              ["Чистое время езды", `${result.pureDrive} ч`],
              ["Итоговое время",    `${result.totalWay} ч`],
              ["Допы",              `${result.extra} ч`],
              ["Остаток вождения",  `${Math.floor(result.driveRemaining)} ч`],
            ].map(([l, v]) => (
              <div key={l} className="stat-row">
                <span className="stat-label">{l}</span>
                <span className="stat-value">{v}</span>
              </div>
            ))}
          </div>
        </div>
        <div className="sep mt-12" style={{marginBottom:12}}></div>
        <div className="result-label">Строка для отчёта</div>
        <div className="code-row">
          <code>{result.workString}</code>
          <button className="copy-btn" onClick={copy}>{copied ? "✓ Скопировано" : "Копировать"}</button>
        </div>
      </div>

      <div className="footer mt-12">Разработал Yaroslav Makarovskyi</div>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
</script>
</body>
</html>
"""

components.html(HTML, height=950, scrolling=True)
