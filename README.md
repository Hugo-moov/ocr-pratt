# Optical Character Recognition

Training material for Pratt and Whitney. It showcases different OCR methods to extract text fields from scanned documents.

Images come from a public dataset available on Hugginface: 

https://huggingface.co/datasets/mychen76/invoices-and-receipts_ocr_v1

## Installation

**Requirements:**
- Python >= 3.13
- Dependencies listed in `requirements.txt`

**Installation:**

```bash
git clone https://github.com/Hugo-moov/ocr-pratt
cd ocr-pratt
pip install -r requirements.txt
```

## Usage

Activate your environment and run the main script:

```bash 
python ocr.py
python azure_document_intelligence.py
```