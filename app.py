import streamlit as st
import pandas as pd
import plotly.express as px

# 1. إعدادات الهوية البصرية (Luxury Dark Theme)
st.set_page_config(page_title="EGISF - Intelligence Portal", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0a0e14; direction: rtl; color: #ffffff; }
    .stMetric { background-color: #16212e; padding: 20px; border-radius: 15px; border-top: 4px solid #d4af37; }
    h1, h2 { color: #d4af37; text-align: center; font-family: 'Arial'; }
    .stSlider > div > div > div > div { background-color: #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# 2. العنوان الرئيسي والشعار
st.title("🏛️ الإطار المتكامل للحوكمة الاستثمارية (EGISF)")
st.subheader("منصة دعم القرار السيادي الذكي - الإصدار العملياتي v1.0")

# 3. لوحة البيانات الرئيسية (KPI Dashboard)
col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("كفاءة الموارد", "94%", "+2%")
with col2: st.metric("السيادة الرقمية", "100%", "آمن")
with col3: st.metric("سرعة الامتثال", "فوري", "رقمي")
with col4: st.metric("مؤشر الهدر", "0.2%", "-0.5%")

st.divider()

# 4. محرك بوابات العبور (Gate Engine)
st.header("⚙️ تقييم بوابات العبور الستة (The Six Gates)")
with st.container():
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🧬 الأبعاد الاستراتيجية")
        strat = st.select_slider("التوافق مع الرؤية", options=["ضعيف", "متوسط", "قوي", "سيادي"])
        eco = st.slider("الجدوى المالية المستدامة", 0, 100, 75)
        soc = st.slider("الأثر المجتمعي والوطني", 0, 100, 80)
    with c2:
        st.markdown("### 🛡️ الأبعاد الرقابية")
        risk = st.slider("تحييد مخاطر التنفيذ", 0, 100, 90)
        gov = st.slider("معايير الامتثال والحوكمة", 0, 100, 100)
        env = st.slider("الاستدامة البيئية (ESG)", 0, 100, 70)

# 5. تحليل البيانات الفوري (Visual Analytics)
st.markdown("---")
data = pd.DataFrame(dict(
    r=[eco, soc, env, risk, gov, 85],
    theta=['المالية','الاجتماعية','البيئية','المخاطر','الحوكمة','الاستراتيجية']))
fig = px.line_polar(data, r='r', theta='theta', line_close=True, template="plotly_dark")
fig.update_traces(fill='toself', fillcolor="rgba(212, 175, 55, 0.3)", line_color="#d4af37")

col_a, col_b = st.columns([1, 2])
with col_a:
    st.header("📊 البصمة الرقمية للمشروع")
    st.write("التحليل الراداري يوضح توازن المشروع بين الربحية والحوكمة.")
    if st.button("توليد تقرير السيادة"):
        st.success("تم تحليل المشروع: مطابق للمعايير السيادية بنسبة 89%")
        st.balloons()
with col_b:
    st.plotly_chart(fig)
