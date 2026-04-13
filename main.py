from auth.google_oauth import authenticate
from sheets.reader import get_emails
from cli.input_handler import get_workshop_details

creds = authenticate()
print("Authentication successful")

emails = get_emails(creds)
print(f"\nFound {len(emails)} emails")

details = get_workshop_details()
print("\nWorkshop details captured:")
print(details)