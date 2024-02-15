import re
from pyrogram import filters
import random
from DAXXMUSIC import app


@app.on_message(filters.command(["gn","n","oodnight","ood Night","ood night"], prefixes=["/","g","G"]))
def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    if send_sticker:
        sticker_id = get_random_sticker()
        app.send_sticker(message.chat.id, sticker_id)
        message.reply_text(f"**Goodnight, {sender}! Sleep tight. 🌙**")
    else:
        emoji = get_random_emoji()
        app.send_message(message.chat.id, emoji)
        message.reply_text(f"**Goodnight, {sender}! Sleep tight. {emoji}**")


def get_random_sticker():
    stickers = [
        "CAACAgQAAx0Cel7IGgACXHllzoQMVwQAAQGvNdx_wBiQ2M6sIHAAAicAAxwS6C_S_blOr4g3vR4E", # Sticker 1
        "CAACAgUAAx0Cel7IGgACXHhlzoPx9EFCgHEfAWZGi6FbhYgZ9AAC1AEAAlvvqVXhd6BuIf0-ox4E", # Sticker 2
        "CAACAgQAAx0Cel7IGgACXIllzoWVmgXLP3neM3MkybAjRiAXTAACGAADHBLoL0UxDdU6sOaAHgQ", # Sticker 3
        "CAACAgQAAx0Cel7IGgACXIxlzoXjDSqAm9Fu5YXg4ET562anxgACJgADHBLoL3UAAVONoOkXyh4E",
        "CAACAgQAAx0Cel7IGgACXJBlzoYZ_9VP2uPg2hzBd8Fkej5G1wACPQADHBLoL0nquLFa0lYwHgQ",
    ]
    return random.choice(stickers)


def get_random_emoji():
    emojis = [
        "😴",
        "😪",
        "💤",
    ]
    return random.choice(emojis)
