"""
Project [DarkWeb](https://github.com/TeamKillerX/DarkWeb) is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import asyncio
import random

import Ubot.modules.basic.truth_and_dare_string as tod

from . import *


# LU GABISA CODING LU KONTOL
# BELAJAR CODING DARI NOL
@Ubot(["apakah"], "")
async def apakah(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("Berikan saya pertanyaan 😐")
    cot = split_text[1]
    await message.reply(f"{random.choice(tod.AP)}")



@Ubot(["kenapa"], "")
async def kenapa(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("Berikan saya pertanyaan 😐")
    cot = split_text[1]
    await message.reply(f"{random.choice(tod.KN)}")


@Ubot(["bagaimana"], "")
async def bagaimana(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("Berikan saya pertanyaan 😐")
    cot = split_text[1]
    await message.reply(f"{random.choice(tod.BG)}")


@Ubot(["dare"], "")
async def dare(client, message):
    try:        
        await message.edit(f"{random.choice(tod.DARE)}")
    except BaseException:
        pass


@Ubot(["truth"], "")
async def truth(client, message):
    try:
        await message.edit(f"{random.choice(tod.TRUTH)}")
    except Exception:
        pass


add_command_help(
    "tod",
    [
        ["dare", "Coba sendiri"],
        ["truth", "Coba sendiri"],
        ["apakah [pertanyaan]", "Coba sendiri"],
        ["kenapa [pertanyaan]", "Coba sendiri"],
        ["bagaimana [pertanyaan]", "Coba sendiri"],
    ],
)

add_command_help(
    "nanya",
    [
        ["apakah [pertanyaan]", "Coba sendiri"],
        ["kenapa [pertanyaan]", "Coba sendiri"],
        ["bagaimana [pertanyaan]", "Coba sendiri"],
    ],
)
        
