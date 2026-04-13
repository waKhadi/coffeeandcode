from auth.google_oauth import authenticate
from sheets.reader import get_emails
from cli.input_handler import get_workshop_details
from mail.sender import render_template

creds = authenticate()
print("Authentication successful")

emails = get_emails(creds)
print(f"\nFound {len(emails)} emails")

details = get_workshop_details()

html = render_template(details)

with open('preview.html', 'w') as f:
    f.write(html)

print("\nTemplate rendered — open preview.html in your browser to view it")