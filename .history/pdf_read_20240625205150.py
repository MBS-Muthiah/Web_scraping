import PyPDF2

pdf_file_obj=open("file1.pdf",'rb')

pdfReader=PyPDF2.PdfFileReader(pdf_file_obj)

print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)

print(pageObj.extract_text())

pdf_file_obj.close()
