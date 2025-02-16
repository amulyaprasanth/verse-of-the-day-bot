import os
import logging
from dotenv import load_dotenv
from instagrapi import Client
from source.image_extraction import get_votd_image

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_env_variables():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    if not username or not password:
        logging.error(
            "Instagram credentials are not set in the environment variables.")
        raise ValueError("Missing Instagram credentials")
    return username, password

def login_to_instagram(client, username, password):
    try:
        logging.info("Logging in to Instagram")
        client.login(username, password)
    except Exception as e:
        logging.error(f"Error logging in to Instagram: {e}")
        raise

def upload_photo(client, photo_path, caption):
    try:
        logging.info(f"Uploading photo: {photo_path} with caption: {caption}")
        client.photo_upload(photo_path, caption)
    except Exception as e:
        logging.error(f"Error uploading photo to Instagram: {e}")
        raise

def main():
    # Get the daily verse from Olive Tree Bible Software
    get_votd_image()

    # Load environment variables
    username, password = load_env_variables()

    # Initialize the client
    client = Client()

    # Log in to Instagram
    login_to_instagram(client, username, password)

    # Upload the photo
    photo_path = "assets/votd.jpg"
    caption = "Today's Bible verse, shared from Olive Tree Bible Software. 📖✨"
    upload_photo(client, photo_path, caption)

    # Log out when done
    logging.info("Logging out of Instagram")
    client.logout()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
