# User Info Service

Telegram bot that displays user information. Similar to @userinfobot.

## Features

- `/start` — shows your Telegram user information
- Forward any message to get information about the original sender
- Handles hidden accounts (when user has restricted forwarding)
- Supports channels and chats as message sources

## Information Displayed

For users:
- User ID
- First name / Last name
- Username
- Language code
- Bot status
- Premium status
- Chat type
- Request timestamp

For forwarded messages:
- Original sender info (if available)
- Hidden user notification (if privacy enabled)
- Channel/chat info (for channel forwards)

## Limitations

This bot only uses official Telegram Bot API. It cannot retrieve:
- Phone numbers
- IP addresses
- Email addresses
- Any other private data not exposed by the API

If a user has enabled "Restrict forwarding" in privacy settings, only their display name will be shown.

## Requirements

- Python >= 3.10
- aiogram 3.22

## Installation

1. Clone the repository:
```bash
git clone https://github.com/NodirUstoz/UserInfoService.git
cd UserInfoService
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```bash
cp .env.example .env
```

5. Add your bot token to `.env`:
```
BOT_TOKEN=your_bot_token_here
```

Get a token from [@BotFather](https://t.me/BotFather).

## Running

```bash
python main.py
```

## Project Structure

```
.
├── handlers/
│   ├── __init__.py
│   └── user.py           # All user-related handlers
├── services/
│   ├── __init__.py
│   └── user_info.py      # User info formatting
├── utils/
│   └── __init__.py
├── main.py               # Entry point
├── config.py             # Configuration
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```