import pdfplumber

PDF_PATH = "samples/invoice_01.pdf"

def main():
    with pdfplumber.open(PDF_PATH) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            print(f"--- Page {page_num} ---")
            text = page.extract_text()
            print(text or "(no text found)")

if __name__ == "__main__":
    main()