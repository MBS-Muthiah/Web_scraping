from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    # Load the image from the file
    image = Image.open(image_path)
    
    # Use pytesseract to do OCR on the image
    extracted_text = pytesseract.image_to_string(image)
    
    return extracted_text

def search_keyword_in_text(text, keyword):
    # Search for the keyword in the text
    if keyword.lower() in text.lower():
        return True
    return False

def main():
    # Path to your image file
    image_path = 'path_to_your_image.jpg'
    
    # The keyword you want to search for
    keyword = 'your_keyword'
    
    # Extract text from the image
    extracted_text = extract_text_from_image(image_path)
    print("Extracted Text:\n", extracted_text)
    
    # Search for the keyword in the extracted text
    if search_keyword_in_text(extracted_text, keyword):
        print(f"Keyword '{keyword}' found in the text.")
    else:
        print(f"Keyword '{keyword}' not found in the text.")

if __name__ == "__main__":
    main()
