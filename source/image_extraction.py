import datetime
import requests
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_current_date():
    now = datetime.datetime.now()
    day = now.strftime("%d")
    month = now.strftime("%m")
    return day, month

def fetch_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching the image: {e}")
        return None

def save_image(image_content, path):
    try:
        with open(path, 'wb') as file:
            file.write(image_content)
        logging.info(f"Image saved to {path}")
    except IOError as e:
        logging.error(f"Error saving the image: {e}")

def get_votd_image():
    day, month = get_current_date()
    votd_url = f"https://votd.olivetree.com/{month}_{day}_NIV.jpg"
    image_content = fetch_image(votd_url)

    if image_content:
        os.makedirs('assets', exist_ok=True)
        image_path = os.path.join('assets', "votd.jpg")
        save_image(image_content, image_path)


if __name__ == "__main__":
    get_votd_image()
