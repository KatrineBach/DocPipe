A small Python tool that turns scanned invoices into structured, DATEV-ready data — so German Mittelstand back offices stop typing the same numbers twice.


# The problem
A 30-person german company still receives most invoices on paper or as PDFs attached to emails. A bookkeeper opens each one, reads the supplier, the invoice number, the date, the line items, the totals — then types them into the accounting system, files the paper, moves on. Three to five minutes per invoice. Multiply by 200 invoices a month and that is roughly a full working day spent on transcription. Skilled work, badly used. It breaks attention, invites typos, and nobody enjoys it.


# Who it's for
Small and mid-sized German companies — roughly 10 to 200 employees — with:

A back office that still handles a noticeable amount of paper or PDF invoices
An accounting workflow built around DATEV or a comparable German system
No in-house software team — they need it to "just work" without a CTO to maintain it

Not for tech startups. For the Tischlerei, the Spedition, the family-owned production company, the regional Steuerberater. The German Mittelstand that the big SaaS players overlook.


# The pipeline
[PDF / scan]  →  [OCR + layout]  →  [Field extraction (ML)]  →  [Rule validation]  →  [DATEV-friendly export]

Ingest — PDFs land in a watched folder, or get forwarded to a dedicated email address.
OCR + layout — read the text and remember where each piece sat on the page (layout matters for invoices).
Field extraction — a small ML model identifies the invoice number, date, supplier, line items, totals, VAT.
Validation — check that totals add up, the VAT ID is plausible, the date is sensible, the supplier is known.
Export — produce a DATEV-compatible export, and flag anything uncertain for the bookkeeper to confirm.

The bookkeeper stays in the loop — DocPipe does the typing, not the deciding.


# Why this, not an off-the-shelf product?


Existing tools are either too generic (built for everyone, fit nobody), too expensive at the small end, or assume a US-style cloud-only deployment that German middle companies are uncomfortable with for data-protection reasons.
A Python-based, self-hostable tool with a DATEV-shaped output fits a real gap.
And — to be honest — building it is also how I rebuild my hands-on stack across Python, ML, FastAPI, Docker, and cloud. Two birds.


# Status
Week 1 of a 48-week build.

✅ Repo created (Week 1, Mon)
✅ Hello-world FastAPI endpoint runs locally (Week 1, Tue)
⏳ Next: ingest a single invoice PDF and print extracted text to console (Week 2)
⏳ Later: OCR + layout, then a first extraction model


# Stack (planned)
Python · FastAPI · Tesseract or PaddleOCR for OCR · a small transformer for field extraction · Docker for packaging · Azure Blob Storage for invoice archives.
