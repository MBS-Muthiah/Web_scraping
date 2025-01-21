import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import qreader

def scrape_image_from_website(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    # Assume the first image is the target
    img_tag = soup.find('img')
    if not img_tag:
        print("No image found on the webpage.")
        return None

    img_url = img_tag.get('src')
    if not img_url:
        print("No image URL found.")
        return None
    
    if not img_url.startswith(('http://', 'https://')):
        img_url = url + img_url

    response = requests.get(img_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the image. Status code: {response.status_code}")
        return None
    
    image = Image.open(BytesIO(response.content))
    return image

def is_qr_code(image):
    qr_data = qreader.detect(image)
    return qr_data is not None

def scan_qr_code(image):
    qr_data = qreader.detect(image)
    if not qr_data:
        print("No QR code found.")
        return None
    
    return qr_data[0]

def search_keyword(text, keyword):
    return keyword in text

def main(url, keyword):
    image = scrape_image_from_website(url)
    if image is None:
        return
    
    if is_qr_code(image):
        print("QR code detected. Scanning...")
        text = scan_qr_code(image)
        if text:
            print(f"QR Code content: {text}")
            if search_keyword(text, keyword):
                print(f"Keyword '{keyword}' found in the QR code content.")
            else:
                print(f"Keyword '{keyword}' not found in the QR code content.")
        else:
            print("Failed to scan the QR code.")
    else:
        print("No QR code detected in the image.")

# Example usage
url = 'https://w3schools.com/'  # Replace with the target website URL
keyword = 'python'  # Replace with the keyword you want to search for
main(url, keyword)
