import streamlit as st
from datetime import datetime, timedelta
import pytz

# Настройка страницы
st.set_page_config(page_title="Logist Pro", layout="centered", page_icon="🚛")

# Красивый и лаконичный CSS
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .stMetric { 
        background-color: #ffffff; 
        padding: 15px; 
        border-radius: 12px; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        border: 1px solid #eee;
    }
    div[data-testid="stExpander"] { border: none !important; box-shadow: none !important; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3em; background-color: #007bff; color: white; }
</style>
""", unsafe_allow_html=True)

# Время CET
cet_zone = pytz.timezone('Europe/Berlin')
now_cet = datetime.now(cet_zone)

# --- ЗАГОЛОВОК ---
st.title("🚛 Logist Calc")
st.caption(f"Текущее время CET: {now_cet.strftime('%H:%M')} | {now_cet.strftime('%d.%m.%Y')}")

# --- БЛОК 1: ОСНОВНЫЕ ДАННЫЕ ---
with st.container():
    col_a, col_b = st.columns(2)
    with col_a:
        dist = st.number_input("Сколько км ехать?", min_value=1, value=500, step=50)
        speed = st.slider("Скорость (км/ч)", 40, 90, 70)
    with col_b:
        mode = st.segmented_control("Режим", ["Одиночка", "Экипаж"], default="Одиночка")
        already_driven = st.number_input("Уже в руле сегодня (ч)", 0.0, 10.0, 0.0, 0.5)

# --- БЛОК 2: ТАХОГРАФ И ДОПЫ (В выпадающем списке, чтобы не путаться) ---
with st.expander("Дополнительные параметры (Паузы, Смена, Загрузки)"):
    c1, c2 = st.columns(2)
    with c1:
        shift_type = st.radio("Лимит смены", ["13 часов", "15 часов"], horizontal=True)
        extra_time = st.number_input("Погрузки / Заправки (часов)", 0.0, 10.0, 0.0, 0.5)
    with c2:
        start_custom = st.checkbox("Изменить время выезда")
        if start_custom:
            t_input = st.time_input("Время старта (CET)", now_cet.time())
            start_dt = cet_zone.localize(datetime.combine(now_cet.date(), t_input))
        else:
            start_dt = now_cet

# --- РАСЧЕТЫ ---
drive_time = dist / speed
# Упрощенная логика пауз
pauses = (drive_time // 4.5) * 0.75 # Каждые 4.5 часа добавляем 45 мин
total_hours = drive_time + pauses + extra_time

# Если руля больше чем осталось на день - добавляем 9ч отстоя
max_daily = 9.0 if shift_type == "13 часов" else 10.0
remaining_drive = max_daily - already_driven

if drive_time > remaining_drive:
    total_hours += 9.0 # Добавляем паузу на сон

eta = start_dt + timedelta(hours=total_hours)

# --- БЛОК 3: РЕЗУЛЬТАТЫ (САМОЕ ВАЖНОЕ) ---
st.divider()

# Основная метрика
st.subheader("🏁 Результат прибытия")
st.metric(label="Ожидаемое время (ETA)", value=eta.strftime('%H:%M'), delta=eta.strftime('%d %b'))

# Вспомогательные метрики
m1, m2, m3 = st.columns(3)
with m1:
    st.metric("В пути", f"{total_hours:.1f} ч")
with m2:
    rem_shift = (13 if shift_type == "13 часов" else 15) - (already_driven + extra_time)
    st.metric("Запас смены", f"{max(0.0, rem_shift):.1f} ч")
with m3:
    st.metric("Чистый руль", f"{drive_time:.1f} ч")

# --- ОТЧЕТ ДЛЯ КОПИРОВАНИЯ ---
st.divider()
st.write("📋 **Строка для отчета:**")
report = f"ETA: {eta.strftime('%d.%m %H:%M')} CET | Остаток руля: {max(0.0, remaining_drive - drive_time):.1f}ч"
st.code(report)
