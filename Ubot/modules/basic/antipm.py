# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


from .apm import get_arg
from pyrogram import filters, Client
from pyrogram.types import Message
from . import *
from Ubot.core.db.pmpermit import pm_guard
from Ubot.core.db import pmpermit as set

@Ubot("antipm", "")
async def pm_permit(client, message):
    arg = get_arg(message)
    user_id = client.me.id
    if not arg:
        await message.reply("**Gunakan format**:\n `antipm` on atau off")
        return
    if arg == "off":
        await set.set_pm(user_id, False)
        await message.edit("**AntiPM Dimatikan**")
    elif arg == "on":
        await set.set_pm(user_id, True)
        await message.edit("**AntiPM Diaktifkan**")

        
@Ubot("setmsg", "")
async def setpmmsg(client, message):
    arg = get_arg(message)
    user_id = client.me.id
    if not arg:
        await message.reply("**Berikan pesan untuk mengatur**\nContoh : `setpm` `Hai apa ada yang bisa saya bantu ?`")
        return
    if arg == "default":
        await set.set_permit_message(user_id, set.PMPERMIT_MESSAGE)
        await message.edit("**Pesan AntiPM Diatur ke Default**.")
        return
    await set.set_permit_message(user_id, f"`{arg}`")
    await message.edit("**Berhasil mengatur pesan AntiPM**")


add_command_help(
    "antipm",
    [
        ["antipm [on or off]", "Hidupkan dan matikan anti-pm."],
        ["setmsg [text or default]", " -> Sets a custom anti-pm message."],
        ["blockmsg [message or default]", "Setel pesan blokir."],
        ["setlimit [angka]", "Peringatan pesan!."],
        ["ok", "Setujui."],
        ["no", "Tolak."],
    ],
)
