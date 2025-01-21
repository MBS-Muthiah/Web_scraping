import PyPDF2

# Open the PDF file in binary read mode
pdf_file_obj = open("file1.pdf", 'rb')


# Create a PdfReader object
pdfReader = PyPDF2.PdfReader(pdf_file_obj)
    
# Get the number of pages
num_pages = len(pdfReader.pages)
print(f"Number of pages: {num_pages}")

    # Get a specific page
page_obj = pdfReader.pages[0]
    
    # Extract text from the page
page_text = page_obj.extract_text()
print(page_text.encode('utf-8'))

    # Close the PDF file
pdf_file_obj.close()
