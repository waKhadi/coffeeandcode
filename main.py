from auth.google_oauth import authenticate
from sheets.reader import get_emails
from cli.input_handler import get_workshop_details
from mail.sender import render_template, send_emails
from config.settings import SENDER_EMAIL

creds = authenticate()
print("Authentication successful")

emails = get_emails(creds)
print(f"\nFound {len(emails)} emails")

details = get_workshop_details()
details['sender_email'] = SENDER_EMAIL

html = render_template(details)

with open('preview.html', 'w') as f:
    f.write(html)

print("\nTemplate rendered — open preview.html to preview before sending")
confirm = input("\nSend emails? (yes/no): ")

if confirm.lower() == 'yes':
    send_emails(creds, emails, details, html)
    print("\nAll emails sent.")
else:
    print("Cancelled.")