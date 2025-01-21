import PyPDF2

# Open the PDF file in binary read mode
pdf_file_obj = open("file1.pdf", 'rb')

try:
    # Create a PdfFileReader object
    pdfReader = PyPDF2.PdfFileReader(pdf_file_obj)
    
    # Get the number of pages
    num_pages = pdfReader.numPages
    print(f"Number of pages: {num_pages}")

    # Get a specific page
    page_obj = pdfReader.getPage(0)
    
    # Extract text from the page
    page_text = page_obj.extract_text()
    print(page_text.encode('utf-8'))
finally:
    # Close the PDF file
    pdf_file_obj.close()
