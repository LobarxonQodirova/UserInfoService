import logging

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from services.user_info import format_forwarded_user_info, format_user_info

router = Router(name="user")
logger = logging.getLogger(__name__)


@router.message(Command("start"))
async def handle_start(message: Message) -> None:
    """Handle /start command. Show greeting and user info."""
    if message.from_user is None:
        await message.answer("Unable to retrieve user information.")
        return

    greeting = "Welcome! Here is your account information:\n\n"
    user_info = format_user_info(message.from_user, message.chat)

    await message.answer(greeting + user_info)
    logger.info("User %d requested their info via /start", message.from_user.id)


@router.message(Command("help"))
async def handle_help(message: Message) -> None:
    """Handle /help command."""
    help_text = (
        "This bot shows Telegram user information.\n\n"
        "Commands:\n"
        "/start - Show your account info\n"
        "/help - Show this message\n\n"
        "Forward a message from any user to see their public info.\n\n"
        "Limitations:\n"
        "- Phone numbers are never available via Bot API\n"
        "- Some users hide their accounts from forwarding\n"
        "- Only public information is displayed"
    )
    await message.answer(help_text)


@router.message(F.forward_origin)
async def handle_forward(message: Message) -> None:
    """Handle forwarded messages. Show info about original sender."""
    user_info = format_forwarded_user_info(message)
    await message.answer(f"Forwarded message info:\n\n{user_info}")

    requester_id = message.from_user.id if message.from_user else "unknown"
    logger.info("User %s requested forward info", requester_id)


@router.message()
async def handle_unknown(message: Message) -> None:
    """Handle any other message."""
    if message.from_user is None:
        await message.answer("Unable to retrieve user information.")
        return

    user_info = format_user_info(message.from_user, message.chat)
    await message.answer(f"Your account information:\n\n{user_info}")
