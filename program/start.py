from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    
        

        reply_markup=InlineKeyboardMarkup(
            
  
 PM_START_TEXT = """
ʜᴏɪ, ɪ ᴍ ᴛɢɴ ʀᴏʙᴏᴛ
`ɪ'ᴍ ʜᴇʀᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘꜱ ᴀɴᴅ ɪ ᴍ ᴠᴇʀʏ ᴘᴏᴡᴇʀꜰᴜʟʟ ʙᴏᴛ! ʜɪᴛ` /help
 [❤](https://telegra.ph/file/cab6825dea9263d347831.jpg)
"""

buttons = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴛɢɴ ʀᴏʙᴏᴛ ᴛᴏ ᴜʀ ᴄʜᴀᴛ", url="t.me/TGN_Ro_bot?startgroup=true"),
    ],
    [
        InlineKeyboardButton(text="ꜱᴏᴜʀᴄᴇ 💫", url=f"https://github.com/Itsunknown-12/TGN-Robot"),
        InlineKeyboardButton(
            text="ꜱᴜᴘᴘᴏʀᴛ ⚡", url=f"https://t.me/{SUPPORT_CHAT}"
        ),
    ],
    [
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇꜱ ☑️", url=f"https://t.me/The_Godfather_Network"),
        InlineKeyboardButton(
            text="ᴛɢɴ ᴄʜᴀᴛ", url=f"https://t.me/greatpersonxd"
        ),
    ],
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", callback_data="help_back"),
    ],
]


HELP_STRINGS = """
`ʏᴏᴜ ᴄᴀɴ ᴄʜᴏᴏꜱᴇ ᴀɴ ᴏᴘᴛɪᴏɴ ʙᴇʟᴏᴡ, ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴀ ʙᴜᴛᴛᴏɴ..`
ᴀʟꜱᴏ ʏᴏᴜ ᴄᴀɴ ᴀꜱᴋ ᴀɴʏᴛʜɪɴɢ ɪɴ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ [❤️](https://telegra.ph/file/cab6825dea9263d347831.jpg)"""
                    
        disable_web_page_preview=True
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✨ Group", url=f"https://t.me/THE_SECRET_WORLDS"),
                InlineKeyboardButton(
                    "📣 Channel", url=f"https://t.me/THE_BLAZE_NETWORK"
                ),
            ]
        ]
    )

    alive = f"**Hello {message.from_user.mention()}, i'm {BOT_NAME}**\n\n✨ Bot is working normally\n🍀 My Master: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n✨ Bot Version: `v{__version__}`\n🍀 Pyrogram Version: `{pyrover}`\n✨ Python Version: `{__python_version__}`\n🍀 PyTgCalls version: `{pytover.__version__}`\n✨ Uptime Status: `{uptime}`\n\n**Thanks for Adding me here, for playing video & music on your Group's video chat** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
