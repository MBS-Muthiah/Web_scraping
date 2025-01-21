import PyPDF2

def find_keyword_in_pdf(pdf_file_path, keyword):
    # Open the PDF file in binary read mode
    with open(pdf_file_path, 'rb') as pdf_file_obj:
        # Create a PdfReader object
        pdfReader = PyPDF2.PdfReader(pdf_file_obj)
        
        # Initialize an empty list to store page numbers
        pages_with_keyword = []
        
        # Iterate through each page
        for page_num in range(len(pdfReader.pages)):
            # Get a specific page
            page_obj = pdfReader.pages[page_num]
            
            # Extract text from the page
            page_text = page_obj.extract_text()
            
            # Check if the keyword is in the extracted text
            if keyword in page_text:
                # Append the page number (starting from 1) to the list
                pages_with_keyword.append(page_num + 1)  # Page numbers are 1-indexed
        
        # Print the results
        if pages_with_keyword:
            print(f"Keyword '{keyword}' found on page(s): {', '.join(map(str, pages_with_keyword))}")
        else:
            print(f"Keyword '{keyword}' not found in the PDF.")

# Example usage
pdf_file_path = "file1.pdf"
keyword_to_find = "example"

find_keyword_in_pdf(pdf_file_path, keyword_to_find)
