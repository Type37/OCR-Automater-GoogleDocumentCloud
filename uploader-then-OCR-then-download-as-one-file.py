import os
import io
import time
from google.cloud import documentai
from pdf2image import convert_from_path

# FPDF not needed anymore unless you still want to create individual PDFs.
# from fpdf import FPDF

# Google Cloud Credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"TKTKTKTTKTK-your-key.json"

#  Google Cloud Document AI Settings
project_id = "" YOUR ID HERE"
location = "us"
processor_id = "a315baae60c00645"
mime_type = "application/pdf"

#  Poppler Custom Path
poppler_path = r"C:\CodingDocs\poppler-24.08.0\Library\bin"

#  Input & Output Folders
input_folder = r"C:\CodingDocs\google-services-cloud\input-docs-individual"
output_folder = r"C:\CodingDocs\google-services-cloud\OCR_PDFs"
os.makedirs(output_folder, exist_ok=True)

# Initialize Google Cloud Document AI Client
client = documentai.DocumentProcessorServiceClient()

def process_pdf_to_text(pdf_file):
    """
    Processes a single PDF, performs OCR via Document AI,
    and returns the extracted text (with page markers).
    """
    pdf_path = os.path.join(input_folder, pdf_file)
    print(f"🔄 Processing: {pdf_file}...")

    # Convert PDF to images
    images = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)

    full_text = ""
    for i, img in enumerate(images):
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format="JPEG")

        raw_doc = documentai.RawDocument(content=img_byte_arr.getvalue(), mime_type="image/jpeg")
        request = documentai.ProcessRequest(
            name=f"projects/{project_id}/locations/{location}/processors/{processor_id}",
            raw_document=raw_doc,
        )

        result = client.process_document(request=request)
        extracted_text = result.document.text

        full_text += f"\n\n--- {pdf_file} - Page {i+1} ---\n{extracted_text}"

        # Wait to avoid potential rate limits
        time.sleep(1)

    return full_text

# ✅ Accumulate text from all files
all_text = ""

for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(".pdf"):
        try:
            extracted_text = process_pdf_to_text(file_name)
            # Append to our big text collector
            all_text += extracted_text
        except Exception as e:
            print(f" ERROR processing {file_name}: {e}")

# ✅ Finally, save the accumulated text to a single text file
output_txt_path = os.path.join(output_folder, "combined_ocr_output.txt")
with open(output_txt_path, "w", encoding="utf-8") as txt_file:
    txt_file.write(all_text)

print(f"🎉 All OCR text combined into: {output_txt_path}")
