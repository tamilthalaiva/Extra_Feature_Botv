"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "Hey There I'm Alive Thanks For Checking On Me π₯°"
REPO = "<b>MY REPO βΊβΊ https://github.com/TechnoMindz/Extra_Feature_Bot</b>"
CHANNEL = "<b>ππΎππππ±π΄ π²π·π°π½π½π΄π»</b> βΊβΊ https://www.youtube.com/channel/UCP07nv5a8HjRd_h_PDQLG6g\n\n<b>ππΏπ³π°ππ΄π π²π·π°π½π½π΄π» βΊβΊ https://t.me/tmmainchannel</b>\n\n<b>π²π·π°π½π½π΄π» βΊβΊ https://t.me/tmmainchannel</b>"
RAVI = "<b>π±πΎπ βΊβΊ https://t.me/TmELsaRoBot</b>"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)


@Client.on_message(filters.command("group", COMMAND_HAND_LER) & f_onw_fliter)
async def group(_, message):
    await message.reply_text(GROUP)


@Client.on_message(filters.command("channel", COMMAND_HAND_LER) & f_onw_fliter)
async def channel(_, message):
    await message.reply_text(CHANNEL)


@Client.on_message(filters.command("ravi", COMMAND_HAND_LER) & f_onw_fliter)
async def ravi(_, message):
    await message.reply_text(RAVI)

#TechnoMindz
