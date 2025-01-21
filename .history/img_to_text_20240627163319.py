import pytesseract

# Add this line to specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from PIL import Image

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

def search_keyword_in_text(text, keyword):
    if keyword.lower() in text.lower():
        return True
    return False

def main():
    image_path = 'path_to_your_image.jpg'
    keyword = 'your_keyword'
    
    extracted_text = extract_text_from_image(image_path)
    print("Extracted Text:\n", extracted_text)
    
    if search_keyword_in_text(extracted_text, keyword):
        print(f"Keyword '{keyword}' found in the text.")
    else:
        print(f"Keyword '{keyword}' not found in the text.")

if __name__ == "__main__":
    main()
