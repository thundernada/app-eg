def calculate_sfm(economic, social, environmental):
    # مؤشر الجدوى الشاملة بناءً على أوزان الميثاق
    weights = {'econ': 0.40, 'soc': 0.30, 'env': 0.30}
    score = (economic * weights['econ']) + (social * weights['soc']) + (environmental * weights['env'])
    return round(score, 2)

def check_governance_gates(scores_dict):
    # بوابات العبور الستة - حد أدنى للنجاح 70%
    threshold = 70
    results = {}
    overall_pass = True
    
    gates = {
        "Gate 1: التوافق الاستراتيجي": scores_dict.get('strategic', 0),
        "Gate 2: الجدوى الاقتصادية": scores_dict.get('economic', 0),
        "Gate 3: القبول الاجتماعي": scores_dict.get('social', 0),
        "Gate 4: الامتثال البيئي": scores_dict.get('environmental', 0),
        "Gate 5: جاهزية المخاطر": scores_dict.get('risk', 0),
        "Gate 6: القدرة المؤسسية": scores_dict.get('governance', 0)
    }
    
    for gate, score in gates.items():
        status = "✅ اجتياز" if score >= threshold else "❌ مراجعة"
        if score < threshold: overall_pass = False
        results[gate] = {"درجة": score, "الحالة": status}
    
    return overall_pass, results