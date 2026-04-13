from dotenv import load_dotenv
import os

load_dotenv()

SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")