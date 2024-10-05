import requests
import PyPDF2
import os
from openai import OpenAI

def download_pdf(url, output_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"PDF downloaded successfully: {output_path}")
    else:
        print(f"Failed to download PDF. Status code: {response.status_code}")

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        text = ''
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extract_text() + '\n'
    return text

def analyze_text_with_openai(text):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Provide an extensive analysis and overview of the following text:\n\n{text}"}
        ]
    )
    return response.choices[0].message

def main():
    pdf_url = "https://www.radarhack.com/tutorial/getting_started_with_OWASP_WebGoat_and_SOAPUI.pdf"
    output_pdf_path = "downloaded_webgoat.pdf"
    
    # Step 1: Download the PDF
    download_pdf(pdf_url, output_pdf_path)
    
    # Step 2: Extract text from the downloaded PDF
    if os.path.exists(output_pdf_path):
        extracted_text = extract_text_from_pdf(output_pdf_path)
        print("Extracted text from PDF:\n")
        print(extracted_text)
        
        # Step 3: Analyze the extracted text with OpenAI
        analysis = analyze_text_with_openai(extracted_text)
        print("\nAnalysis of the extracted text:\n")
        print(analysis)
    else:
        print("PDF file not found.")

if __name__ == "__main__":
    main()
