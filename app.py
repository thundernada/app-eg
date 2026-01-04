import streamlit as st
from logic import calculate_sfm, check_governance_gates
from processor import process_excel, process_pdf

# إعداد واجهة برؤية احترافية
st.set_page_config(page_title="منصة EGISF الذكية", layout="wide", initial_sidebar_state="expanded")

# تنسيق CSS لجعل الخطوط من اليمين لليسار (عربي)
st.markdown("""
    <style>
    .reportview-container { direction: rtl; }
    .main { text-align: right; }
    </style>
    """, unsafe_allow_context=True)

st.title("🏛️ نظام EGISF للحوكمة ودعم القرار الاستثماري")
st.info("تحويل الميثاق التأسيسي إلى محرك ذكاء اصطناعي لضمان صفر هدر وسيادة رقمية.")

# لوحة التحكم الجانبية
with st.sidebar:
    st.header("📂 مركز رفع البيانات")
    ex_file = st.file_uploader("ارفع جدول التكاليف (Excel)", type=['xlsx'])
    pdf_file = st.file_uploader("ارفع دراسة الجدوى (PDF)", type=['pdf'])
    st.markdown("---")
    st.write("تم تطويره بناءً على ميثاق استراتيجية EGISF 2025")

# منطقة العرض الرئيسية
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 مدخلات التقييم الذكي")
    # إذا تم رفع ملف PDF يتم تحديث السلايدر تلقائياً
    pdf_score = process_pdf(pdf_file) if pdf_file else 50
    
    econ_input = st.slider("معيار الكفاءة المالية", 0, 100, 75)
    soc_input = st.slider("معيار الأثر المجتمعي", 0, 100, 65)
    env_input = st.slider("معيار الاستدامة البيئية (من الـ PDF)", 0, 100, int(pdf_score))

# حساب النتائج
sfm_score = calculate_sfm(econ_input, soc_input, env_input)
gates_input = {
    'strategic': 80, 'economic': econ_input, 'social': soc_input, 
    'environmental': env_input, 'risk': 70, 'governance': 85
}
is_passed, gate_details = check_governance_gates(gates_input)

with col2:
    st.subheader("📊 مؤشر الجدوى الشاملة (SFM)")
    st.metric(label="درجة المشروع الإجمالية", value=f"{sfm_score}%", delta=f"{sfm_score-70}% من حد الأمان")
    
    if is_passed:
        st.success("✅ المشروع مطابق لمعايير بوابات العبور")
    else:
        st.warning("⚠️ المشروع يحتاج لإعادة ضبط ليتوافق مع الحوكمة")

st.markdown("---")
st.subheader("🔍 تفصيل حالة بوابات العبور (6 Gates)")
# عرض النتائج في شكل أعمدة
cols = st.columns(3)
for i, (gate, data) in enumerate(gate_details.items()):
    with cols[i % 3]:
        st.info(f"**{gate}**\n\n النتيجة: {data['درجة']} | {data['الحالة']}")

# رسم توضيحي بسيط