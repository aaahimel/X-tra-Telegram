"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**No Name set yet.** [Check Guide.](https://how2techy.com/xtra-guide1/)"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`Currently Alive, my master!` **ψ(｀∇´)ψ**\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\n`"
                     "`Bot created by:` [whi5tLe_bL0w3R](tg://some_unsupported_feature)\n"
                     f"`My owner`: {DEFAULTUSER}\n\n"
                     "[View My Profile](tg://need_update_for_some_feature)")
