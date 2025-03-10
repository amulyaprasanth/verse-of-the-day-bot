import os
import logging
import time
import random
from dotenv import load_dotenv
from instagrapi import Client
from source.image_extraction import get_votd_image

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_env_variables():
    load_dotenv()
    username = os.getenv("INSTAGRAM_USERNAME")
    password = os.getenv("INSTAGRAM_PASSWORD")
    if not username or not password:
        logging.error("Instagram credentials are not set in the environment variables.")
        raise ValueError("Missing Instagram credentials")
    return username, password

def login_to_instagram(client, username, password):
    try:
        if os.path.exists("session.json"):
            logging.info("Loading existing session...")
            client.load_settings("session.json")
        else:
            logging.info("Logging in to Instagram...")
            client.login(username, password)
            client.dump_settings("session.json")
        time.sleep(random.uniform(3, 7))  # Add delay to mimic human behavior
    except Exception as e:
        logging.error(f"Error logging in to Instagram: {e}")
        raise

def upload_photo(client, photo_path, caption):
    try:
        logging.info(f"Uploading photo: {photo_path} with caption: {caption}")
        client.photo_upload(photo_path, caption)
        time.sleep(random.uniform(5, 10))  # Delay to mimic human behavior
    except Exception as e:
        logging.error(f"Error uploading photo to Instagram: {e}")
        raise

def main():
    # Get the daily verse
    get_votd_image()

    # Load environment variables
    username, password = load_env_variables()

    # Initialize the client
    client = Client()

    # Log in to Instagram
    login_to_instagram(client, username, password)

    # Upload the photo
    photo_path = "assets/votd.jpg"
    captions = [
        "Today's Bible verse, shared from Olive Tree Bible Software. 📖✨",
        "Start your day with some inspiration!,  shared from Olive Tree Bible Software. 📜 #BibleVerse",
        "A powerful verse to reflect on today, shared from Olive Tree Bible Software. 🙏 #DailyVerse",
        "Be encouraged with today's Bible verse, shared from Olive Tree Bible Software.  ✨ #Faith"
    ]
    caption = random.choice(captions)  # Rotate captions for variety
    upload_photo(client, photo_path, caption)

    # Log out only if necessary (prefer session persistence)
    logging.info("Session saved; no need to log out.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
