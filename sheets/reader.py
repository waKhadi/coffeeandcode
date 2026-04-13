import re
from googleapiclient.discovery import build
from config.settings import SHEET_ID

def is_valid_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None

def get_emails(creds):
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    result = sheet.values().get(
        spreadsheetId=SHEET_ID,
        range='A:Z'
    ).execute()

    values = result.get('values', [])

    if not values:
        print("No data found in sheet")
        return []

    headers = values[0]

    try:
        email_col = next(i for i, h in enumerate(headers) if 'email' in h.lower())
    except StopIteration:
        print("No email column found")
        return []

    emails = []
    for row in values[1:]:
        if len(row) > email_col:
            email = row[email_col].strip()
            if is_valid_email(email):
                emails.append(email)
            else:
                print(f"Skipping invalid email: {email}")

    return emails