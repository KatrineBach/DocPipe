import re
import pdfplumber

PDF_PATH = "samples/invoice_02.pdf"

def read_text(path):
    with pdfplumber.open(path) as pdf:
        return  "\n".join(p.extract_text() or "" for p in pdf.pages)

def extraxt(text):
    invoice_no = re.search(r"(?:Rechnung|Invoice Number)[\s*[:#]?\s*(\S+)", text, re.I)
    date = re.search(r"(\d{2}\.\d{2}\.\d{4})", text)
    total = re.search(r"(?:Gesamt|Total|Brutto|Endbetrag)[^\n]*?(\d{1,3}(?:[.,]\d{3})*[.,]\d{2})", text, re.I)
    return {
        "invoice_no": invoice_no.group(1) if invoice_no else None,
        "date": date.group(1) if date else None,
        "total": total.group(1) if total else None,

    }

def parse_amount(s):
    """'2.840,00' or '2,840.00' -> 2840.00 (float)."""
    s = s.strip()
    if ',' in s and '.' in s:
        # Whichever separator is LAST is the decimal point
        if s.rindex(',') > s.rindex('.'):
            s = s.replace('.', '').replace(',', '.')   # German
        else:
            s = s.replace(',', '')                      # English
    elif ',' in s:
        s = s.replace(',', '.')                         # comma-only = German decimal
    return float(s)

date_patterns = [
    r"(\d{1,2}\.\d{1,2}\.\d{4})",                                                # 25.01.2016
    r"(\d{4}-\d{1,2}-\d{1,2})",                                                   # 2016-01-25 (ISO)
    r"((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4})",  # January 25, 2016
    r"(\d{1,2}\.\s*(?:Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)\s+\d{4})",  # 25. Januar 2016
]

def find_date(text):
    for p in date_patterns:
        m = re.search(p, text, re.I)
        if m:
            return m.group(1)
    return None

if __name__ == "__main__":
    text = read_text(PDF_PATH)
    print(extraxt(text))



