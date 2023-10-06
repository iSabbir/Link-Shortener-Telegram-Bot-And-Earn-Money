#This Project Is Made By iSabbir , Give Proper Credit 💚

import re
import aiohttp

from os import environ
from pyrogram import Client, filters
from pyrogram.types import *

API_ID = "SET TELEGRAM API ID"
API_HASH = "SET TELEGRAM API HASH"
BOT_TOKEN = "SET TELEGRAM BOT TOKEN FROM BotFather"
API_KEY = "SET HERE SHORTENER API"
API_URL = "SET API URL HERE , CHECK REPO FOR ALL LINKS"

bdbots = Client('link shortener bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=100)

print("🚀 Developer: @BDBots , Join & Share Channel")
print("🤖 Bot is Started Now")

#This Project Is Made By iSabbir , Give Proper Credit 💚

@bdbots.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hello {message.chat.first_name}!** 🙌\n\n"
        "I'm Link Shortener bot. Just send me a link and get a short link. You can also send multiple links separated by a space or enter.\n\n**Developer:** @BDBots",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Source Code", url="https://github.com/iSabbir/Link-Shortener-Telegram-Bot-And-Earn-Money"),
             InlineKeyboardButton("Subscribe", url="https://bdbots.t.me/")]
        ]))

#This Project Is Made By iSabbir , Give Proper Credit 💚

@bdbots.on_message(filters.private & filters.text & filters.incoming)
async def link_handler(bot, message):
    link_pattern = re.compile('https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}', re.DOTALL)
    links = re.findall(link_pattern, message.text)
    if len(links) <1:
        await message.reply("❌ No links Found in this text",quote=True)
        return
    for link in links:
        try:
            short_link = await get_shortlink(link)
            await message.reply(f"✨ 𝐇𝐞𝐫𝐞 𝐢𝐬 𝐘𝐨𝐮𝐫 𝐒𝐡𝐨𝐫𝐭𝐞𝐧𝐞𝐝 𝐋𝐢𝐧𝐤 ✨\n\n𝐎𝐫𝐢𝐠𝐢𝐧𝐚𝐥 𝐋𝐢𝐧𝐤: {link}\n\n𝐒𝐡𝐨𝐫𝐭𝐞𝐧𝐞𝐝 𝐋𝐢𝐧𝐤: `{short_link}`",quote=True,disable_web_page_preview=True)
        except Exception as e:
            await message.reply(f'❌ 𝐄𝐫𝐫𝐨𝐫: `{e}`', quote=True)

async def get_shortlink(link):
    url = API_URL
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]

bdbots.run()

#Hello Bro , i Know You Are Pro , Huge Respect For You , Sir 🤗
#This Project Is Made By iSabbir , Give Proper Credit 💚
