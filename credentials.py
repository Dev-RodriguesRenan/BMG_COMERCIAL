import os
from dotenv import load_dotenv

load_dotenv()

email_credentials = {
    "user": os.getenv("EMAIL_USER"),
    "password": os.getenv("EMAIL_PASSWORD"),
    "receivers": os.getenv("EMAIL_RECEIVER").split(","),
}
