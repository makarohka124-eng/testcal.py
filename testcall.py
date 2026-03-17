import streamlit as st
from datetime import datetime, timedelta
import pytz
import math

# Настройка страницы
st.set_page_config(page_title="Logist Calc Pro", layout="wide", page_icon="🚛")

# Продвинутый CSS для профессионального интерфейса
st.markdown("""
<style>
    /* Основной фон и шрифты */
    .stApp { background-color: #f4f7f9; }
    
    /* Стилизация блоков */
    div[data-testid="stVerticalBlock"] > div {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.03);
        margin-bottom: 10px;
    }
    
    /* Стили для заголовков */
    h1, h2, h3 { color: #1e293b !important; font-weight: 700 !important; }
    
    /* Убираем лишние отступы */
    .block-container { padding-top: 2rem; }
    
    /* Красивая подпись */
    .footer {
        position: fixed;
        left: 20px;
        bottom: 20px;
        color: #94a3b8;
        font-size: 12px;
        font-weight: 500;
    }

    /* Стиль для метрик */
    [data-testid="stMetricValue"] { font-size: 24px !important; color: #0f172a; }
</style>
""", unsafe_allow_html=True)

# Время CET
cet_zone = pytz.timezone('Europe/Berlin')
now_cet = datetime.now(cet_zone)

# --- ШАПКА ---
st.title("🚛 Logist Pro Calc")
st.markdown(f"**Текущее время в Европе:** `{now_cet.strftime('%H:%M')} CET` | `{now_cet.strftime('%d.%m.%Y')}`")

# --- ЛИНИЯ 1: СТАРТ РЕЙСА ---
with st.container():
    st.subheader("⏱️ Время отправления")
    c1, c2, c3 = st.columns([1, 1.5, 2.5])
    
    with c1:
        use_current = st.checkbox("Сейчас", value=True, key="use_curr")
    with c2:
        if not use_current:
            start_date = st.date_input("Дата выезда", now_cet.date())
        else:
            st.info(f"📅 {now_cet.strftime('%d.%m')}")
    with c3:
        if not use_current:
            start_time = st.time_input("Время (CET)", now_cet.time())
            start_dt = cet_zone.localize(datetime.combine(start_date, start_time))
        else:
            start_dt = now_cet
            st.info(f"🕒 {now_cet.strftime('%H:%M')} CET")

# --- ЛИНИЯ 2: ПАРАМЕТРЫ И ДОПЫ ---
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.subheader("🚩 Маршрут и режим")
    sub_c1, sub_c2 = st.columns(2)
    with sub_c1:
        dist = st.number_input("Расстояние, км:", min_value=1, value=1000, step=10)
        speed = st.slider("Средняя скорость:", 40, 90, 70)
    with sub_c2:
        mode = st.segmented_control("Режим работы:", ["Одиночка", "Экипаж"], default="Одиночка")
        limit = 9.0 if mode == "Одиночка" else 18.0
        already_driven = st.number_input("Уже проехал (ч):", 0.0, limit, 0.0, 0.5)

with col_right:
    st.subheader("➕ Остановки и задержки")
    sub_c3, sub_c4 = st.columns(2)
    with sub_c3:
        ferry_time_val = st.selectbox("Паром:", ["Нет", "1 час", "2 часа"])
        misc = st.selectbox("Прочее (ч):", [0, 1, 2, 3, 4, 5])
    with sub_c4:
        st.write("**Доп. опции:**")
        gas = st.checkbox("⛽ Заправка (+1ч)")
        trailer = st.checkbox("🔄 Перецеп (+1ч)")
        loading = st.checkbox("📦 Загрузка (+2ч)")

# --- МАТЕМАТИКА ---
extra_time = (1 if gas else 0) + (1 if trailer else 0) + (2 if loading else 0) + misc
ferry_h = 1 if "1 час" in ferry_time_val else (2 if "2 часа" in ferry_time_val else 0)

pure_drive = dist / speed
current_left = max(0.0, limit - already_driven)

if mode == "Одиночка":
    if pure_drive <= current_left:
        drive_remaining = current_left - pure_drive
        total_breaks = 1 if (already_driven < 4.5 and (already_driven + pure_drive) > 4.5) else 0
        total_rests = 0
    else:
        rem_after = pure_drive - current_left
        rests_count = math.ceil(rem_after / 9)
        drive_remaining = 9 - (rem_after % 9) if rem_after % 9 != 0 else 9
        total_breaks = (1 if already_driven < 4.5 else 0) + (math.floor(rem_after / 9) * 2) + (1 if (rem_after % 9) > 4.5 else 0)
        total_rests = rests_count * 9.0
    total_way = pure_drive + total_breaks + total_rests + ferry_h + extra_time
else:
    rests_count = math.ceil((pure_drive - current_left) / 18) if pure_drive > current_left else 0
    drive_remaining = current_left - pure_drive if rests_count == 0 else 18 - ((pure_drive - current_left) % 18)
    total_way = pure_drive + (rests_count * 9.0) + ferry_h + extra_time

arrival = start_dt + timedelta(hours=total_way)

# --- БЛОК РЕЗУЛЬТАТОВ ---
st.divider()
res_c1, res_c2 = st.columns([1, 1])

with res_c1:
    st.subheader("🏁 Итог прибытия")
    st.metric(label="Время ETA (CET)", value=arrival.strftime('%H:%M'), delta=arrival.strftime('%d.%m | %A'))
    st.info(f"Общее время в пути: **{total_way:.1f} ч.**")

with res_c2:
    st.subheader("📝 Отчет")
    check_val = "1/2" if now_cet.hour < 12 else "2/2"
    work_string = f"{check_val} ETA  {arrival.strftime('%d.%m %H:%M')}CET D/H {int(drive_remaining)}"
    st.code(work_string, language="text")
    st.caption("Нажми на иконку справа в поле выше, чтобы скопировать")

# Подпись
st.markdown('<div class="footer">👨‍💻 Создал: Yaroslav Makarovskyi</div>', unsafe_allow_html=True)
