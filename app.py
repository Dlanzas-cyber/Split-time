import streamlit as st
from datetime import datetime, timedelta

def split_time(start_str, end_str, cuts=1, overlap_minutes=0):
    start = datetime.strptime(start_str, "%H:%M")
    end = datetime.strptime(end_str, "%H:%M")
    total_duration = (end - start).total_seconds() / 60

    if total_duration <= 0:
        raise ValueError("A hora de fim deve inferior à hora de inicio.")
    if cuts < 1:
        raise ValueError("Deve haver pelo menos um corte.")

    periods = cuts + 1
    result = []

    if overlap_minutes > 0:
        segment_duration = total_duration / periods
        adjusted_duration = segment_duration + overlap_minutes
        for i in range(periods):
            seg_start = start + timedelta(minutes=segment_duration * i)
            seg_end = seg_start + timedelta(minutes=adjusted_duration)
            if seg_end > end:
                seg_end = end
            result.append((seg_start.strftime("%H:%M"), seg_end.strftime("%H:%M")))
    else:
        segment_duration = total_duration / periods
        for i in range(periods):
            seg_start = start + timedelta(minutes=segment_duration * i)
            seg_end = seg_start + timedelta(minutes=segment_duration)
            result.append((seg_start.strftime("%H:%M"), seg_end.strftime("%H:%M")))

    return result

st.title("🕐 Split-Time App")
st.write("Divide um periodo de tempo en periodos iguais, com ou sem sobreposição.")

col1, col2 = st.columns(2)
with col1:
    start_time = st.time_input("Hora de inicio", value=datetime.strptime("23:00", "%H:%M").time())
with col2:
    end_time = st.time_input("Hora de fim", value=datetime.strptime("07:30", "%H:%M").time())

cuts = st.number_input("Número de cortes", min_value=1, value=1)

overlap_enabled = st.checkbox("¿Queres sobreposição?")
overlap_minutes = 0
if overlap_enabled:
    overlap_minutes = st.slider("Minutos de sobreposição", 1, 120, 15)

if st.button("Calcular"):
    try:
        start_str = start_time.strftime("%H:%M")
        end_str = end_time.strftime("%H:%M")
        blocks = split_time(start_str, end_str, cuts, overlap_minutes if overlap_enabled else 0)

        st.subheader("📋 Periodos gerados:")
        for i, (ini, fin) in enumerate(blocks, 1):
            st.write(f"**Periodo {i}:** {ini} - {fin}")
    except Exception as e:
        st.error(f"Ocurrió um error: {e}")
