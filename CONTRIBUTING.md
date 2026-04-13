\# Contributing to coffeeandcode



Thanks for your interest in contributing. This project was built at WeThinkCode\_ 

to automate workshop email notifications for the Coffee \& Code community.

All contributions are welcome as long as they follow this process.



\---



\## Before You Start



Every contribution must be linked to an existing issue.

If the issue doesn't exist, open one first and describe what you want to build or fix.

No issue, no pull request.



\---



\## Setup



\### 1. Fork the repo



Click Fork on GitHub. This gives you your own copy to work on.



\### 2. Clone your fork



git clone https://github.com/YOUR\_USERNAME/coffeeandcode.git

cd coffeeandcode



\### 3. Create a virtual environment



python -m venv venv

venv\\Scripts\\activate       # Windows

source venv/bin/activate    # Linux/Mac



\### 4. Install dependencies



pip install -r requirements.txt



\### 5. Set up Google Cloud



\- Go to console.cloud.google.com

\- Create a new project

\- Enable Gmail API and Google Sheets API

\- Go to Credentials → Create OAuth 2.0 Client ID → Desktop App

\- Download the JSON, rename it credentials.json, place it in config/

\- Add yourself as a test user under OAuth consent screen → Test Users



\### 6. Configure your environment



Copy .env.example to .env and fill in your values:



GOOGLE\_SHEET\_ID=your\_sheet\_id\_here

SENDER\_EMAIL=your\_email@student.wethinkcode.co.za



\---



\## Contribution Flow



\### 1. Create a branch off main



Name it after what you are building:



git checkout -b feat/your-feature-name

git checkout -b fix/what-you-are-fixing



\### 2. Build it



Keep changes focused. One issue, one branch, one pull request.

Do not bundle multiple fixes or features into a single PR.



\### 3. Test it



Run the script end to end before opening a PR:



python main.py



Make sure nothing that was working before is now broken.



\### 4. Commit clearly



git add .

git commit -m "feat: short description of what you built"

git commit -m "fix: short description of what you fixed"



\### 5. Push and open a Pull Request



git push origin your-branch-name



Go to GitHub, open a Pull Request to main, and link the issue it resolves.



\---



\## Rules



\- Never commit .env, credentials.json, or token.json

\- Never push directly to main

\- Every PR must reference an issue

\- Keep PRs small and focused



\---



\## Project Structure



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



\---



\## License



By contributing you agree that your contributions will be licensed under the MIT License.

