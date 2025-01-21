import cv2
import requests
from bs4 import BeautifulSoup

def scan_qr_code(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image not found or unable to open.")
    
    # Initialize QRCodeDetector
    detector = cv2.QRCodeDetector()
    
    # Detect and decode the QR code
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    if data:
        return data
    else:
        raise ValueError("No QR code found in the image.")

def fetch_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the website content: {e}")
        return None

def search_keyword_in_html(html_content, keyword):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Search for the keyword in the text of the website
    results = soup.find_all(string=lambda text: text and keyword.lower() in text.lower())
    return results

# Main function
if __name__ == "__main__":
    qr_code_path = 'D:\\web scraping\\w3 schools.png'  # Replace with the actual path to your QR code image
    keyword = 'python'  # Replace with the keyword you want to search for
    
    try:
        url = scan_qr_code(qr_code_path)
        print(f"URL from QR code: {url}")
        
        if url:
            html_content = fetch_website_content(url)
            if html_content:
                search_results = search_keyword_in_html(html_content, keyword)
                print(f"Found {len(search_results)} results containing the keyword '{keyword}':")
                for result in search_results:
                    print(result.strip())
    except ValueError as e:
        print(e)
