# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import html
import time
import asyncio
from pyrogram import Client, enums
from pyrogram.types import Message
from . import *
from ubotlibs.ubot.helper.basic import edit_or_reply
from ubotlibs.ubot.helper.parser import mention_html, mention_markdown


@Ubot(["admin"], "")
async def adminlist(client: Client, message: Message):
    toolong = False
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
    else:
        chat = message.chat.id
    grup = await client.get_chat(chat)
    replyid = message.reply_to_message.id if message.reply_to_message else None
    creator = []
    admin = []
    badmin = []
    async for a in client.get_chat_members(
        message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
    ):
        try:
            nama = f"{a.user.first_name} {a.user.last_name}"
        except:
            nama = a.user.first_name
        if nama is None:
            nama = "☠️ Deleted account"
        if a.status == enums.ChatMemberStatus.ADMINISTRATOR:
            if a.user.is_bot:
                badmin.append(mention_markdown(a.user.id, nama))
            else:
                admin.append(mention_markdown(a.user.id, nama))
        elif a.status == enums.ChatMemberStatus.OWNER:
            creator.append(mention_markdown(a.user.id, nama))
    admin.sort()
    badmin.sort()
    totaladmins = len(creator) + len(admin) + len(badmin)
    teks = f"**Daftar Admin Di {grup.title}**\n" + "**Pemilik**\n"
    for x in creator:
        teks += f"• {x}\n\n"
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += f"\n**{len(admin)} Admin**\n"
    for x in admin:
        teks += f"• {x}\n"
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += f"\n**{len(badmin)} Bot Admin**\n"
    for x in badmin:
        teks += f"• {x}\n"
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += f"\n**Total {totaladmins} Admins**"
    if toolong:
        await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
    else:
        await message.reply(teks)


@Ubot(["zombies"], "")
async def kickdel_cmd(client: Client, message: Message):
    kk = await message.reply("<b>Membersihkan akun depresi...</b>")
    try:
        values = [
            await message.chat.ban_member(
                member.user.id, datetime.now() + timedelta(seconds=31)
            )
            async for member in client.get_chat_members(message.chat.id)
            if member.user.is_deleted
        ]
    except Exception as e:
        return await message.edit(format_exc(e))
    await asyncio.sleep(0.1)
    await kk.delete()
    await message.edit(
        f"<b>Berhasil ditendang {len(values)} akun depresi (s)</b>"
    )


@Ubot("report", "")
async def report_admin(client: Client, message: Message):
    await message.delete()
    if len(message.text.split()) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        text = None
    grup = await client.get_chat(message.chat.id)
    admin = []
    async for a in client.get_chat_members(
        message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
    ):
        if (
            a.status
            in [
                enums.ChatMemberStatus.ADMINISTRATOR,
                enums.ChatMemberStatus.OWNER,
            ]
            and not a.user.is_bot
        ):
            admin.append(mention_html(a.user.id, "\u200b"))
    if message.reply_to_message:
        teks = (
            f"{text}"
            if text
            else f"{mention_html(message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name)} reported to admins."
        )
    else:
        teks = f"{html.escape(text)}" if text else f"Calling admins in {grup.title}."
    teks += "".join(admin)
    if message.reply_to_message:
        await client.send_message(
            message.chat.id,
            teks,
            reply_to_message_id=message.reply_to_message.id,
            parse_mode=enums.ParseMode.HTML,
        )
    else:
        await client.send_message(
            message.chat.id, teks, parse_mode=enums.ParseMode.HTML
        )


@Ubot("tagall", "")
async def tag_all_users(client: Client, message: Message):
    await message.delete()
    if len(message.text.split()) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        text = "Hi all 🙃"
    kek = client.get_chat_members(message.chat.id)
    async for a in kek:
        if not a.user.is_bot:
            text += mention_html(a.user.id, "\u200b")
    if message.reply_to_message:
        await client.send_message(
            message.chat.id,
            text,
            reply_to_message_id=message.reply_to_message.id,
            parse_mode=enums.ParseMode.HTML,
        )
    else:
        await client.send_message(
            message.chat.id, text, parse_mode=enums.ParseMode.HTML
        )


@Ubot(["Bots"], "")
async def get_list_bots(client: Client, message: Message):
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
    else:
        chat = message.chat.id
    grup = await client.get_chat(chat)
    replyid = message.reply_to_message.id if message.reply_to_message else None
    getbots = client.get_chat_members(chat)
    bots = []
    async for a in getbots:
        try:
            nama = f"{a.user.first_name} {a.user.last_name}"
        except:
            nama = a.user.first_name
        if nama is None:
            nama = "☠️ Deleted account"
        if a.user.is_bot:
            bots.append(mention_markdown(a.user.id, nama))
    teks = f"**Daftar Bot Di {grup.title}**\n" + "Bots\n"
    for x in bots:
        teks += f"• {x}\n"
    teks += f"Total {len(bots)} Bot"
    if replyid:
        await client.send_message(message.chat.id, teks, reply_to_message_id=replyid)
    else:
        await message.reply(teks)

add_command_help(
    "misc",
    [
        ["admins", "Get chats Admins list."],
        ["zombies", "To Kick deleted Accounts."],
        ["botlist", "To get Chats Bots list"],
    ],
)