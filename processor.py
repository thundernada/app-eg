import pandas as pd
import pdfplumber

def process_excel(file):
    try:
        df = pd.read_excel(file)
        # محاكاة استخراج أرقام: نبحث عن إجمالي التكاليف أو الأرباح
        total_investment = df.iloc[:, 1].sum() if not df.empty else 0
        return {"investment": total_investment, "status": "Success"}
    except:
        return {"investment": 0, "status": "Error reading Excel"}

def process_pdf(file):
    try:
        with pdfplumber.open(file) as pdf:
            text = " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
        
        # البحث عن كلمات مفتاحية لتقييم الالتزام بالميثاق
        keywords = ["استدامة", "حوكمة", "مخاطر", "سيادة", "تحول رقمي"]
        found = [word for word in keywords if word in text]
        score = (len(found) / len(keywords)) * 100
        return round(score, 2)
    except:
        return 0