from datetime import datetime, timezone

from aiogram.types import Chat, Message, User


def format_user_info(user: User, chat: Chat) -> str:
    """Format user information into a readable string."""
    lines = [
        f"ID: {user.id}",
        f"First name: {user.first_name}",
    ]

    if user.last_name:
        lines.append(f"Last name: {user.last_name}")

    if user.username:
        lines.append(f"Username: @{user.username}")

    lines.append(f"Bot: {'Yes' if user.is_bot else 'No'}")

    if user.language_code:
        lines.append(f"Language: {user.language_code}")

    if user.is_premium:
        lines.append("Premium: Yes")

    lines.append(f"Chat type: {chat.type}")
    lines.append(f"Requested: {_format_timestamp()}")

    return "\n".join(lines)


def format_forwarded_user_info(message: Message) -> str:
    """Format information about forwarded message sender."""
    forward_origin = message.forward_origin

    if forward_origin is None:
        return "No forward information available."

    origin_type = forward_origin.type
    lines: list[str] = []

    if origin_type == "user":
        user = forward_origin.sender_user
        lines = [
            f"ID: {user.id}",
            f"First name: {user.first_name}",
        ]
        if user.last_name:
            lines.append(f"Last name: {user.last_name}")
        if user.username:
            lines.append(f"Username: @{user.username}")
        lines.append(f"Bot: {'Yes' if user.is_bot else 'No'}")
        if user.language_code:
            lines.append(f"Language: {user.language_code}")
        if user.is_premium:
            lines.append("Premium: Yes")

    elif origin_type == "hidden_user":
        sender_name = forward_origin.sender_user_name
        lines = [
            "Privacy enabled: Yes",
            f"Sender name: {sender_name}",
            "",
            "Note: User has hidden their account from forwarded messages.",
        ]

    elif origin_type == "chat":
        chat = forward_origin.sender_chat
        lines = [
            f"Chat ID: {chat.id}",
            f"Title: {chat.title or 'N/A'}",
            f"Type: {chat.type}",
        ]
        if chat.username:
            lines.append(f"Username: @{chat.username}")

    elif origin_type == "channel":
        chat = forward_origin.chat
        lines = [
            f"Channel ID: {chat.id}",
            f"Title: {chat.title or 'N/A'}",
        ]
        if chat.username:
            lines.append(f"Username: @{chat.username}")
        if forward_origin.message_id:
            lines.append(f"Message ID: {forward_origin.message_id}")

    else:
        lines = [f"Unknown forward origin type: {origin_type}"]

    lines.append(f"Requested: {_format_timestamp()}")
    return "\n".join(lines)


def _format_timestamp() -> str:
    """Return current UTC timestamp in readable format."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
