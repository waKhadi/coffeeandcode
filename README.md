# coffeeandcode

A lightweight Python tool that automates workshop email notifications to participants using Google Sheets, Gmail API, and a custom HTML template.

Built by Khadi — Coffee & Code, WeThinkCode_.

---

## Requirements

- Python 3.10+
- A Google account with access to Gmail and Google Sheets
- A Google Cloud project with Gmail API and Sheets API enabled

---

## Setup

### 1. Clone the repo

git clone https://github.com/waKhadi/coffeeandcode.git
cd coffeeandcode

### 2. Create a virtual environment

python -m venv venv
venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Google Cloud Setup

- Go to console.cloud.google.com
- Create a new project
- Enable Gmail API and Google Sheets API
- Go to Credentials → Create OAuth 2.0 Client ID → Desktop App
- Download the JSON and rename it credentials.json
- Place it inside the config/ folder

### 5. Configure environment variables

Copy .env.example to .env and fill in your values:

GOOGLE_SHEET_ID=your_sheet_id_here
SENDER_EMAIL=your_email@student.wethinkcode.co.za

Your Sheet ID is the string in your Google Sheet URL between /d/ and /edit.

### 6. Add yourself as a test user

- Go to APIs & Services → OAuth consent screen
- Scroll to Test Users → add your Google account email

---

## Usage

python main.py

The script will:
1. Authenticate with your Google account
2. Read participant emails from your Google Sheet
3. Prompt you for workshop details
4. Render a preview HTML email — open preview.html in your browser before sending
5. Ask for confirmation before sending

---

## Project Structure

coffeeandcode/
├── auth/           # Google OAuth authentication
├── cli/            # Terminal input handler
├── config/         # Settings and environment variables
├── mail/           # Email rendering and sending
│   └── templates/  # HTML email templates
├── sheets/         # Google Sheets reader
├── main.py         # Entry point
├── requirements.txt
├── .env.example
└── README.md

---

## License

MIT