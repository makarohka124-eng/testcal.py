import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Logist Calc", layout="wide", page_icon="🚛")
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
  --bg:#f8f8f8;--bg2:#f0f0f1;--bg3:#e4e4e7;
  --fg:#09090b;--fg2:#71717a;
  --border:rgba(0,0,0,0.1);--border2:rgba(0,0,0,0.2);
  --card:#fff;--muted:#f4f4f5;
  --success-bg:#f0fdf4;--success-fg:#166534;--success-bd:#bbf7d0;
  --danger-bg:#fef2f2;--danger-fg:#991b1b;--danger-bd:#fecaca;
  --primary:#09090b;--primary-fg:#fafafa;
  --break-bg:#fef3c7;--break-fg:#92400e;
  --rest-bg:#ede9fe;--rest-fg:#4c1d95;
  --break-dot:#f59e0b;--rest-dot:#6366f1;
}
.dark{
  --bg:#0a0a0b;--bg2:#111113;--bg3:#27272a;
  --fg:#fafafa;--fg2:#a1a1aa;
  --border:rgba(255,255,255,0.08);--border2:rgba(255,255,255,0.16);
  --card:#18181b;--muted:#27272a;
  --success-bg:#052e16;--success-fg:#86efac;--success-bd:#166534;
  --danger-bg:#450a0a;--danger-fg:#fca5a5;--danger-bd:#991b1b;
  --primary:#fafafa;--primary-fg:#09090b;
  --break-bg:#451a03;--break-fg:#fcd34d;
  --rest-bg:#2e1065;--rest-fg:#c4b5fd;
  --break-dot:#f59e0b;--rest-dot:#818cf8;
}
html,body{height:100%;overflow:hidden}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:var(--bg);color:var(--fg);font-size:13px}

/* ---- LAYOUT ---- */
.shell{
  display:grid;
  grid-template-rows:auto 1fr;
  height:100vh;
  padding:10px 12px 8px;
  gap:8px;
}
.topbar{
  display:flex;align-items:center;gap:10px;
  padding:0 2px;
}
.main{
  display:grid;
  grid-template-columns:220px 220px 1fr;
  gap:8px;
  min-height:0;
}
.col{display:flex;flex-direction:column;gap:8px;min-height:0;overflow:hidden}
.result-col{display:flex;flex-direction:column;gap:8px;min-height:0;overflow:hidden}

/* ---- CARD ---- */
.card{
  background:var(--card);
  border:0.5px solid var(--border);
  border-radius:10px;
  padding:10px 12px;
  flex-shrink:0;
}
.card.scroll{overflow-y:auto;flex:1;min-height:0}
.ct{font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--fg2);margin-bottom:8px}

/* ---- FORM ---- */
.fl{display:block;font-size:11px;color:var(--fg2);margin-bottom:3px}
.row{margin-bottom:8px}
.row:last-child{margin-bottom:0}
input[type=number],input[type=date],input[type=text],select{
  width:100%;height:28px;padding:0 8px;
  background:var(--bg2);border:0.5px solid var(--border2);
  border-radius:6px;color:var(--fg);font-size:12px;
  font-family:inherit;outline:none;
}
input:focus,select:focus{border-color:var(--fg2)}
input[type=range]{width:100%;accent-color:var(--fg);cursor:pointer;height:3px}
.rval{font-size:12px;font-weight:500;min-width:32px;text-align:right}

/* ---- SWITCH ---- */
.sw{position:relative;width:30px;height:17px;flex-shrink:0}
.sw input{opacity:0;width:0;height:0}
.sw-t{position:absolute;inset:0;background:var(--border2);border-radius:100px;transition:background .18s;cursor:pointer}
.sw input:checked+.sw-t{background:var(--primary)}
.sw-t::after{content:'';position:absolute;width:11px;height:11px;left:3px;top:3px;background:#fff;border-radius:50%;transition:transform .18s}
.sw input:checked+.sw-t::after{transform:translateX(13px)}
.sw-row{display:flex;align-items:center;gap:8px;cursor:pointer;user-select:none}

/* ---- RADIO ---- */
.rg{display:flex;gap:4px}
.rb{flex:1;height:26px;display:flex;align-items:center;justify-content:center;border:0.5px solid var(--border2);border-radius:6px;font-size:11px;cursor:pointer;background:var(--bg2);color:var(--fg);transition:all .12s;user-select:none}
.rb.on{background:var(--primary);color:var(--primary-fg);border-color:var(--primary)}

/* ---- BADGE ---- */
.badge{display:inline-flex;align-items:center;padding:1px 6px;border-radius:100px;font-size:10px;font-weight:500;background:var(--bg3);color:var(--fg2)}
.tz-badge{display:inline-flex;align-items:center;padding:1px 7px;border-radius:100px;font-size:10px;font-weight:600;background:var(--primary);color:var(--primary-fg)}

/* ---- SEP ---- */
.sep{height:0.5px;background:var(--border);margin:6px 0}

/* ---- ALERT ---- */
.alert{padding:6px 10px;border-radius:6px;border:0.5px solid;font-size:12px;display:flex;align-items:center;gap:6px}
.alert-s{background:var(--success-bg);border-color:var(--success-bd);color:var(--success-fg)}
.alert-d{background:var(--danger-bg);border-color:var(--danger-bd);color:var(--danger-fg)}

/* ---- STAT ROWS ---- */
.stat{display:flex;justify-content:space-between;align-items:center;padding:4px 0;border-bottom:0.5px solid var(--border)}
.stat:last-child{border-bottom:none}
.sl{font-size:11px;color:var(--fg2)}
.sv{font-size:12px;font-weight:500;color:var(--fg)}

/* ---- ARRIVAL BIG ---- */
.arrival-time{font-size:17px;font-weight:700;color:var(--fg);line-height:1.2;margin-bottom:2px}
.arrival-sub{font-size:11px;color:var(--fg2)}

/* ---- CODE ROW ---- */
.code-row{display:flex;align-items:center;gap:8px;background:var(--muted);border-radius:6px;padding:7px 10px}
.code-row code{flex:1;font-family:monospace;font-size:12px;color:var(--fg);word-break:break-all}
.copy-btn{height:24px;padding:0 9px;flex-shrink:0;border:0.5px solid var(--border2);border-radius:6px;background:var(--card);color:var(--fg);font-size:11px;cursor:pointer;font-family:inherit}
.copy-btn:hover{background:var(--bg3)}

/* ---- TIMELINE ---- */
.tl{display:flex;flex-direction:column}
.tl-row{display:flex;align-items:stretch}
.tl-dc{display:flex;flex-direction:column;align-items:center;width:20px;flex-shrink:0}
.tl-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0;margin-top:2px}
.tl-dot.drive{background:var(--primary)}
.tl-dot.break{background:var(--break-dot)}
.tl-dot.rest{background:var(--rest-dot)}
.tl-line{width:1.5px;flex:1;min-height:4px;background:var(--border2)}
.tl-body{padding:0 0 8px 6px;flex:1}
.tl-lbl{font-size:12px;font-weight:500;color:var(--fg)}
.tl-tag{display:inline-flex;align-items:center;padding:0px 6px;border-radius:100px;font-size:10px;font-weight:500;margin-left:5px}
.tl-tag.drive{background:var(--bg3);color:var(--fg2)}
.tl-tag.break{background:var(--break-bg);color:var(--break-fg)}
.tl-tag.rest{background:var(--rest-bg);color:var(--rest-fg)}
.leg{display:flex;gap:10px;margin-bottom:8px;flex-wrap:wrap}
.leg-i{display:flex;align-items:center;gap:4px;font-size:10px;color:var(--fg2)}
.leg-d{width:7px;height:7px;border-radius:50%;flex-shrink:0}

/* ---- TIME PICKER ---- */
.tp{background:var(--bg2);border-radius:6px;padding:8px 10px}
.tp-disp{font-size:20px;font-weight:700;font-family:monospace;color:var(--fg);text-align:center;margin-bottom:6px;letter-spacing:2px}
.tp-row{display:flex;align-items:center;gap:6px;margin-bottom:4px}
.tp-row:last-child{margin-bottom:0}
.tp-lbl{font-size:10px;color:var(--fg2);width:24px;flex-shrink:0}
.tp-val{font-size:11px;font-weight:500;width:20px;text-align:right;color:var(--fg);flex-shrink:0}
.tp-inp{display:flex;align-items:center;gap:6px;margin-top:6px}
.tp-inp span{font-size:10px;color:var(--fg2);flex-shrink:0}
.tp-inp input{width:70px;text-align:center;font-family:monospace;font-size:12px;height:24px}

/* topbar */
.tb-title{font-size:15px;font-weight:700;color:var(--fg)}
.tb-sub{font-size:11px;color:var(--fg2)}
.theme-btn{width:28px;height:28px;border:0.5px solid var(--border2);border-radius:50%;background:var(--bg2);color:var(--fg);cursor:pointer;font-size:13px;display:flex;align-items:center;justify-content:center}
.theme-btn:hover{background:var(--bg3)}
.footer{font-size:10px;color:var(--fg2);text-align:right;padding:2px 0}
</style>
</head>
<body>
<div id="root"></div>
<script type="text/babel">
const { useState, useMemo, useEffect } = React;

const TIMEZONES = [
  { label:"CET — Берлин/Варшава",  tz:"Europe/Berlin" },
  { label:"EET — Киев/Рига",       tz:"Europe/Kiev" },
  { label:"MSK — Москва",          tz:"Europe/Moscow" },
  { label:"GMT — Лондон",          tz:"Europe/London" },
  { label:"UTC",                    tz:"UTC" },
  { label:"TRT — Стамбул",         tz:"Europe/Istanbul" },
  { label:"FET — Минск",           tz:"Europe/Minsk" },
];

function getNowInTZ(tz){ return new Date(new Date().toLocaleString("en-US",{timeZone:tz})); }
function pad(n){ return String(n).padStart(2,"0"); }
function todayISO(tz){ const d=getNowInTZ(tz); return `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}`; }
function tomorrowISO(tz){ const d=getNowInTZ(tz); d.setDate(d.getDate()+1); return `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}`; }
function localeDateRu(date,tz){
  return date.toLocaleString("ru-RU",{timeZone:tz,weekday:"short",day:"2-digit",month:"2-digit",hour:"2-digit",minute:"2-digit",hour12:false});
}

function buildSchedule({alreadyDriven,pureDrive,mode}){
  const steps=[];
  if(mode==="single"){
    const left=Math.max(0,9-alreadyDriven);
    if(pureDrive<=left){
      if(alreadyDriven<4.5&&alreadyDriven+pureDrive>4.5){
        const d1=4.5-alreadyDriven;
        steps.push({type:"drive",h:d1},{type:"break",h:1},{type:"drive",h:pureDrive-d1});
      } else { steps.push({type:"drive",h:pureDrive}); }
    } else {
      if(alreadyDriven<4.5){
        const d1=4.5-alreadyDriven, d2=left-d1;
        steps.push({type:"drive",h:d1},{type:"break",h:1});
        if(d2>0) steps.push({type:"drive",h:d2});
      } else { if(left>0) steps.push({type:"drive",h:left}); }
      steps.push({type:"rest",h:9});
      let rem=pureDrive-left;
      while(rem>0){
        const blk=Math.min(9,rem);
        if(blk>4.5){
          steps.push({type:"drive",h:4.5},{type:"break",h:1},{type:"drive",h:blk-4.5});
        } else { steps.push({type:"drive",h:blk}); }
        rem-=blk;
        if(rem>0){ steps.push({type:"break",h:1},{type:"rest",h:9}); }
      }
    }
  } else {
    const left=Math.max(0,18-alreadyDriven);
    if(pureDrive<=left){ steps.push({type:"drive",h:pureDrive}); }
    else {
      if(left>0) steps.push({type:"drive",h:left});
      steps.push({type:"rest",h:9});
      let rem=pureDrive-left;
      while(rem>0){
        const blk=Math.min(18,rem);
        steps.push({type:"drive",h:blk});
        rem-=blk;
        if(rem>0) steps.push({type:"rest",h:9});
      }
    }
  }
  return steps;
}

function calcArrival({useCurrent,startDate,startHour,startMin,tz,dist,speed,mode,alreadyDriven,gas,trailer,loading,ferry,misc}){
  let startDt;
  if(useCurrent){ startDt=getNowInTZ(tz); }
  else {
    const naive=new Date(`${startDate}T${pad(startHour)}:${pad(startMin)}:00`);
    const tzNow=new Date(naive.toLocaleString("en-US",{timeZone:tz}));
    startDt=new Date(naive.getTime()+(naive-tzNow));
  }
  const extra=(gas?1:0)+(trailer?1:0)+(loading?2:0)+Number(misc)+Number(ferry);
  const pureDrive=dist/speed;
  const limit=mode==="single"?9:18;
  const left=Math.max(0,limit-alreadyDriven);
  let totalWay,driveRemaining,restBlocks,breaks45;
  if(mode==="single"){
    if(pureDrive<=left){
      const nb=alreadyDriven<4.5&&alreadyDriven+pureDrive>4.5?1:0;
      totalWay=pureDrive+nb; driveRemaining=left-pureDrive; restBlocks=0; breaks45=nb;
    } else {
      const rem=pureDrive-left, shifts=Math.ceil(rem/9);
      totalWay=pureDrive+shifts*9+(alreadyDriven<4.5?1:0)+shifts*2;
      driveRemaining=rem%9!==0?9-(rem%9):9; restBlocks=shifts; breaks45=(alreadyDriven<4.5?1:0)+shifts*2;
    }
  } else {
    const shifts=pureDrive>left?Math.ceil((pureDrive-left)/18):0;
    totalWay=pureDrive+shifts*9;
    driveRemaining=shifts===0?left-pureDrive:18-((pureDrive-left)%18);
    restBlocks=shifts; breaks45=0;
  }
  const schedule=buildSchedule({alreadyDriven,pureDrive,mode});
  totalWay+=extra;
  const arrival=new Date(startDt.getTime()+totalWay*3600000);
  const cetNow=getNowInTZ("Europe/Berlin");
  const checkVal=cetNow.getHours()<12?"1/2":"2/2";
  const a=new Date(arrival.toLocaleString("en-US",{timeZone:"Europe/Berlin"}));
  const workString=`${checkVal} ETA ${pad(a.getDate())}.${pad(a.getMonth()+1)} ${pad(a.getHours())}:${pad(a.getMinutes())}CET D/H ${Math.floor(driveRemaining)}`;
  return {arrival,workString,driveRemaining,pureDrive:pureDrive.toFixed(1),totalWay:totalWay.toFixed(1),extra,restBlocks,breaks45,schedule};
}

function Sw({id,checked,onChange}){
  return <label className="sw"><input type="checkbox" id={id} checked={checked} onChange={e=>onChange(e.target.checked)}/><span className="sw-t"/></label>;
}

function TP({hour,minute,onH,onM}){
  const [raw,setRaw]=useState(`${pad(hour)}:${pad(minute)}`);
  const [focused,setFocused]=useState(false);
  useEffect(()=>{ if(!focused) setRaw(`${pad(hour)}:${pad(minute)}`); },[hour,minute,focused]);
  function handleChange(e){
    setRaw(e.target.value);
    const m=e.target.value.match(/^(\d{1,2}):(\d{2})$/);
    if(m){ onH(Math.min(23,+m[1])); onM(Math.min(59,+m[2])); }
  }
  return (
    <div className="tp">
      <div className="tp-disp">{pad(hour)}:{pad(minute)}</div>
      <div className="tp-row">
        <span className="tp-lbl">Ч</span>
        <input type="range" min="0" max="23" value={hour} onChange={e=>onH(+e.target.value)} style={{flex:1}}/>
        <span className="tp-val">{pad(hour)}</span>
      </div>
      <div className="tp-row">
        <span className="tp-lbl">М</span>
        <input type="range" min="0" max="59" value={minute} onChange={e=>onM(+e.target.value)} style={{flex:1}}/>
        <span className="tp-val">{pad(minute)}</span>
      </div>
      <div className="tp-inp">
        <span>ввод:</span>
        <input type="text" value={raw} placeholder="14:30"
          onFocus={()=>setFocused(true)}
          onChange={handleChange}
          onBlur={()=>{setFocused(false);setRaw(`${pad(hour)}:${pad(minute)}`);}}/>
      </div>
    </div>
  );
}

function App(){
  const [tz,setTz]=useState("Europe/Berlin");
  const [dark,setDark]=useState(()=>window.matchMedia("(prefers-color-scheme: dark)").matches);
  const [useCurrent,setUseCurrent]=useState(true);
  const [startDate,setStartDate]=useState(()=>todayISO("Europe/Berlin"));
  const [startHour,setStartHour]=useState(()=>getNowInTZ("Europe/Berlin").getHours());
  const [startMin,setStartMin]=useState(()=>getNowInTZ("Europe/Berlin").getMinutes());
  const [dist,setDist]=useState(1000);
  const [speed,setSpeed]=useState(70);
  const [mode,setMode]=useState("single");
  const [already,setAlready]=useState(0);
  const [useFix,setUseFix]=useState(false);
  const [fixDate,setFixDate]=useState(()=>tomorrowISO("Europe/Berlin"));
  const [fixH,setFixH]=useState(8);
  const [fixM,setFixM]=useState(0);
  const [gas,setGas]=useState(false);
  const [trailer,setTrailer]=useState(false);
  const [loading,setLoading]=useState(false);
  const [ferry,setFerry]=useState("0");
  const [misc,setMisc]=useState("0");
  const [copied,setCopied]=useState(false);

  useEffect(()=>{ document.documentElement.className=dark?"dark":""; },[dark]);
  useEffect(()=>{ if(useCurrent){ const n=getNowInTZ(tz); setStartHour(n.getHours()); setStartMin(n.getMinutes()); setStartDate(todayISO(tz)); } },[tz]);

  const maxDrive=mode==="single"?9:18;
  const now=getNowInTZ(tz);
  const tzShort=TIMEZONES.find(t=>t.tz===tz)?.label.split("—")[0].trim()||tz;

  const result=useMemo(()=>calcArrival({useCurrent,startDate,startHour,startMin,tz,dist,speed,mode,alreadyDriven:already,gas,trailer,loading,ferry,misc}),
    [useCurrent,startDate,startHour,startMin,tz,dist,speed,mode,already,gas,trailer,loading,ferry,misc]);

  const arrivalLabel=useMemo(()=>localeDateRu(result.arrival,tz),[result.arrival,tz]);

  const fixDiff=useMemo(()=>{
    if(!useFix) return null;
    const naive=new Date(`${fixDate}T${pad(fixH)}:${pad(fixM)}:00`);
    const tzNow=new Date(naive.toLocaleString("en-US",{timeZone:tz}));
    const fixDt=new Date(naive.getTime()+(naive-tzNow));
    return (fixDt.getTime()-result.arrival.getTime())/3600000;
  },[useFix,fixDate,fixH,fixM,tz,result.arrival]);

  const fdH=fixDiff!==null?Math.floor(Math.abs(fixDiff)):0;
  const fdM=fixDiff!==null?Math.round((Math.abs(fixDiff)%1)*60):0;
  const fixOk=fixDiff!==null&&fixDiff>=0;

  function copy(){
    try{
      const ta=document.createElement("textarea"); ta.value=result.workString;
      ta.style.position="fixed"; ta.style.opacity="0";
      document.body.appendChild(ta); ta.focus(); ta.select();
      document.execCommand("copy"); document.body.removeChild(ta);
      setCopied(true); setTimeout(()=>setCopied(false),1500);
    }catch(e){}
  }

  const tlLabels={drive:"Езда",break:"Перерыв 45мин",rest:"Отдых 9ч"};
  const tlSub={drive:s=>`${s.h.toFixed(1)} ч`,break:()=>"= 1ч",rest:()=>"9ч"};

  return (
    <div className="shell">
      {/* TOPBAR */}
      <div className="topbar">
        <span style={{fontSize:16}}>🚛</span>
        <span className="tb-title">Калькулятор рейса</span>
        <span className="tb-sub">·</span>
        <span className="tz-badge">{tzShort}</span>
        <select value={tz} onChange={e=>setTz(e.target.value)}
          style={{height:24,fontSize:11,padding:"0 6px",background:"var(--bg2)",border:"0.5px solid var(--border2)",borderRadius:6,color:"var(--fg)",fontFamily:"inherit",outline:"none",width:200}}>
          {TIMEZONES.map(t=><option key={t.tz} value={t.tz}>{t.label}</option>)}
        </select>
        <button className="theme-btn" style={{marginLeft:"auto"}} onClick={()=>setDark(d=>!d)}>{dark?"☀️":"🌙"}</button>
        <span className="footer" style={{marginLeft:8}}>by Yaroslav Makarovskyi</span>
      </div>

      {/* MAIN 3-COL */}
      <div className="main">

        {/* COL 1 — ВЫЕЗД + РЕЙС */}
        <div className="col">
          <div className="card">
            <div className="ct">Выезд</div>
            <div className="row">
              <div className="sw-row">
                <Sw id="uc" checked={useCurrent} onChange={setUseCurrent}/>
                <label htmlFor="uc" style={{cursor:"pointer",fontSize:12}}>
                  Сейчас <span style={{color:"var(--fg2)"}}>{pad(now.getHours())}:{pad(now.getMinutes())}</span>
                </label>
              </div>
            </div>
            {!useCurrent && (<>
              <div className="row">
                <label className="fl">Дата</label>
                <input type="date" value={startDate} onChange={e=>setStartDate(e.target.value)}/>
              </div>
              <div className="row">
                <label className="fl">Время</label>
                <TP hour={startHour} minute={startMin} onH={setStartHour} onM={setStartMin}/>
              </div>
            </>)}
          </div>

          <div className="card" style={{flex:1}}>
            <div className="ct">Параметры рейса</div>
            <div className="row">
              <label className="fl">Расстояние (км)</label>
              <input type="number" min="1" value={dist} onChange={e=>setDist(+e.target.value)}/>
            </div>
            <div className="row">
              <div style={{display:"flex",justifyContent:"space-between",marginBottom:3}}>
                <span className="fl" style={{margin:0}}>Скорость</span>
                <span className="rval">{speed} км/ч</span>
              </div>
              <input type="range" min="40" max="90" value={speed} onChange={e=>setSpeed(+e.target.value)}/>
              <div style={{display:"flex",justifyContent:"space-between"}}>
                <span style={{fontSize:10,color:"var(--fg2)"}}>40</span>
                <span style={{fontSize:10,color:"var(--fg2)"}}>90</span>
              </div>
            </div>
            <div className="row">
              <label className="fl">Режим</label>
              <div className="rg">
                <div className={`rb ${mode==="single"?"on":""}`} onClick={()=>setMode("single")}>Одиночка</div>
                <div className={`rb ${mode==="crew"?"on":""}`} onClick={()=>setMode("crew")}>Экипаж</div>
              </div>
            </div>
            <div className="row">
              <div style={{display:"flex",justifyContent:"space-between",marginBottom:3}}>
                <span className="fl" style={{margin:0}}>Уже проехал (ч)</span>
                <span style={{fontSize:10,color:"var(--fg2)"}}>макс {maxDrive}ч</span>
              </div>
              <input type="number" min="0" max={maxDrive} step="0.5" value={already}
                onChange={e=>setAlready(Math.min(maxDrive,+e.target.value))}/>
            </div>
          </div>
        </div>

        {/* COL 2 — ДОПЫ */}
        <div className="col">
          <div className="card" style={{flex:1}}>
            <div className="ct">Дополнительно</div>

            <div className="row">
              <div className="sw-row">
                <Sw id="uf" checked={useFix} onChange={setUseFix}/>
                <label htmlFor="uf" style={{cursor:"pointer",fontSize:12}}>Фикс время выгрузки</label>
              </div>
            </div>
            {useFix && (<>
              <div className="row" style={{paddingLeft:38}}>
                <label className="fl">Дата FIX</label>
                <input type="date" value={fixDate} onChange={e=>setFixDate(e.target.value)}/>
              </div>
              <div className="row" style={{paddingLeft:38}}>
                <label className="fl">Время FIX</label>
                <TP hour={fixH} minute={fixM} onH={setFixH} onM={setFixM}/>
              </div>
            </>)}

            <div className="sep"/>
            <div style={{fontSize:10,color:"var(--fg2)",textTransform:"uppercase",letterSpacing:".07em",marginBottom:6}}>Остановки</div>
            {[
              {id:"g",label:"Заправка",plus:"+1ч",val:gas,set:setGas},
              {id:"tr",label:"Перецеп",plus:"+1ч",val:trailer,set:setTrailer},
              {id:"ld",label:"Загрузка",plus:"+2ч",val:loading,set:setLoading},
            ].map(({id,label,plus,val,set})=>(
              <div key={id} className="row">
                <div className="sw-row">
                  <Sw id={id} checked={val} onChange={set}/>
                  <label htmlFor={id} style={{cursor:"pointer",fontSize:12,display:"flex",gap:5,alignItems:"center"}}>
                    {label} <span className="badge">{plus}</span>
                  </label>
                </div>
              </div>
            ))}

            <div className="sep"/>
            <div className="row">
              <label className="fl">Паром</label>
              <select value={ferry} onChange={e=>setFerry(e.target.value)}>
                <option value="0">Нет</option><option value="1">1 час</option><option value="2">2 часа</option>
              </select>
            </div>
            <div className="row">
              <label className="fl">Другое (ч)</label>
              <select value={misc} onChange={e=>setMisc(e.target.value)}>
                {[0,1,2,3,4,5].map(v=><option key={v} value={v}>{v}</option>)}
              </select>
            </div>
          </div>
        </div>

        {/* COL 3 — РЕЗУЛЬТАТ */}
        <div className="result-col">
          {/* Arrival + stats */}
          <div className="card">
            <div className="ct">Результат</div>
            <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:12,alignItems:"start"}}>
              <div>
                <div style={{fontSize:10,color:"var(--fg2)",marginBottom:4}}>Прибытие</div>
                <div className="arrival-time">{arrivalLabel}</div>
                {useFix&&fixDiff!==null&&(
                  <div className={`alert mt-4 ${fixOk?"alert-s":"alert-d"}`} style={{marginTop:6}}>
                    {fixOk?`✓ Запас: ${fdH}ч ${fdM}м`:`✗ Опоздание: ${fdH}ч ${fdM}м`}
                  </div>
                )}
              </div>
              <div>
                {[
                  ["Езда чистая",`${result.pureDrive} ч`],
                  ["Итого",`${result.totalWay} ч`],
                  ["Допы",`${result.extra} ч`],
                  ["Остаток",`${Math.floor(result.driveRemaining)} ч`],
                  ["Отдыхов",`${result.restBlocks}`],
                  ["Перерывов 45'",`${result.breaks45}`],
                ].map(([l,v])=>(
                  <div key={l} className="stat">
                    <span className="sl">{l}</span>
                    <span className="sv">{v}</span>
                  </div>
                ))}
              </div>
            </div>
            <div style={{marginTop:8}}>
              <div style={{fontSize:10,color:"var(--fg2)",marginBottom:4}}>Строка для отчёта</div>
              <div className="code-row">
                <code>{result.workString}</code>
                <button className="copy-btn" onClick={copy}>{copied?"✓ OK":"Копировать"}</button>
              </div>
            </div>
          </div>

          {/* Timeline */}
          <div className="card scroll">
            <div className="ct">Режим труда и отдыха</div>
            <div className="leg">
              <span className="leg-i"><span className="leg-d" style={{background:"var(--primary)"}}/>Езда</span>
              <span className="leg-i"><span className="leg-d" style={{background:"var(--break-dot)"}}/>Перерыв 45мин</span>
              <span className="leg-i"><span className="leg-d" style={{background:"var(--rest-dot)"}}/>Отдых 9ч</span>
            </div>
            <div className="tl">
              {result.schedule.map((s,i)=>{
                const isLast=i===result.schedule.length-1;
                return (
                  <div key={i} className="tl-row">
                    <div className="tl-dc">
                      <div className={`tl-dot ${s.type}`}/>
                      {!isLast&&<div className="tl-line"/>}
                    </div>
                    <div className="tl-body">
                      <span className="tl-lbl">{tlLabels[s.type]}</span>
                      <span className={`tl-tag ${s.type}`}>{tlSub[s.type](s)}</span>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>

      </div>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(<App/>);
</script>
</body>
</html>
"""

components.html(HTML, height=780, scrolling=False)
