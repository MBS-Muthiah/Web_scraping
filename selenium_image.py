from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import io
from PIL import Image
import time
import os

# Use the Service object for initializing the webdriver
service = Service(ChromeDriverManager().install())
wd = webdriver.Chrome(service=service)

def get_images_from_google(wd, delay, max_images):
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)

    url = "https://www.google.com/search?q=cats&tbm=isch"
    wd.get(url)

    image_urls = set()
    skips = 0

    while len(image_urls) + skips < max_images:
        scroll_down(wd)

        thumbnails = wd.find_elements(By.CLASS_NAME, "H8Rx8c")

        for img in thumbnails[len(image_urls) + skips:max_images]:
            try:
                img.click()
                time.sleep(delay)
            except Exception as e:
                print(f"Error clicking thumbnail: {e}")
                continue

            images = wd.find_elements(By.CLASS_NAME, "YsLeY")
            for image in images:
                src = image.get_attribute('src')
                if src in image_urls:
                    max_images += 1
                    skips += 1
                    break

                if src and 'http' in src:
                    image_urls.add(src)
                    print(f"Found {len(image_urls)} images")

    return image_urls

def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = os.path.join(download_path, file_name)

        with open(file_path, "wb") as f:
            image.save(f, "JPEG")

        print(f"Success: {file_name}")
    except Exception as e:
        print(f"FAILED - {e}")

# Ensure the directory exists
if not os.path.exists("imgs"):
    os.makedirs("imgs")

# Get image URLs and download them
urls = get_images_from_google(wd, 1, 6)
for i, url in enumerate(urls):
    download_image("imgs", url, f"{i}.jpg")

wd.quit()
