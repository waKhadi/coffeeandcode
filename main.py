from auth.google_oauth import authenticate
from sheets.reader import get_emails

creds = authenticate()
print("Authentication successful")

emails = get_emails(creds)
print(f"Found {len(emails)} emails:")
for email in emails:
    print(email)