import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from googleapiclient.discovery import build


def render_template(details):
    with open('mail/templates/workshop.html', 'r') as f:
        template = f.read()

    for key, value in details.items():
        template = template.replace('{{' + key + '}}', value)

    return template


def send_emails(creds, emails, details, html):
    service = build('gmail', 'v1', credentials=creds)

    for recipient in emails:
        message = MIMEMultipart('alternative')
        message['Subject'] = f"Coffee & Code Workshop: {details['name']}"
        message['From'] = details['sender_email']
        message['To'] = recipient

        message.attach(MIMEText(html, 'html'))

        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        service.users().messages().send(
            userId='me',
            body={'raw': raw}
        ).execute()

        print(f"Sent to {recipient}")