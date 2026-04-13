import sys
from auth.google_oauth import authenticate
from sheets.reader import get_emails
from cli.input_handler import get_workshop_details
from mail.sender import render_template, send_emails
from config.settings import SENDER_EMAIL

def main():
    if not SENDER_EMAIL:
        print("ERROR: SENDER_EMAIL is missing from your .env file")
        sys.exit(1)

    try:
        creds = authenticate()
        print("Authentication successful")
    except Exception as e:
        print(f"Authentication failed: {e}")
        sys.exit(1)

    try:
        emails = get_emails(creds)
    except Exception as e:
        print(f"Failed to read Google Sheet: {e}")
        sys.exit(1)

    if not emails:
        print("No valid emails found. Exiting.")
        sys.exit(0)

    print(f"\nFound {len(emails)} valid emails")

    details = get_workshop_details()
    details['sender_email'] = SENDER_EMAIL

    try:
        html = render_template(details)
    except Exception as e:
        print(f"Failed to render template: {e}")
        sys.exit(1)

    with open('preview.html', 'w') as f:
        f.write(html)

    print("\nTemplate rendered — open preview.html to preview before sending")
    confirm = input("\nSend emails? (yes/no): ")

    if confirm.lower() != 'yes':
        print("Cancelled.")
        sys.exit(0)

    failed = []
    for recipient in emails:
        try:
            send_emails(creds, [recipient], details, html)
            print(f"Sent to {recipient}")
        except Exception as e:
            print(f"Failed to send to {recipient}: {e}")
            failed.append(recipient)

    print(f"\nDone. {len(emails) - len(failed)} sent, {len(failed)} failed.")
    if failed:
        print("Failed recipients:")
        for f in failed:
            print(f"  - {f}")

if __name__ == "__main__":
    main()