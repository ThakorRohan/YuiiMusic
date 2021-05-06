from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hello 👋 there! I'm Tohka! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\n🔴 Do you want me to play music in your Telegram groups'voice chats? Please click the \'📜 User Manual 📜\' button below to know how you can use me.\n\n🔴 The Assistant must be in your group to play music in the voice chat of your group.""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Add me to groups", url="t.me/TohkaMusic_bot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "📜 User Manual 📜", url="https://telegra.ph/Tohka-Yatogami-04-20"
                    ), 
                    InlineKeyboardButton(
                        "Group", url="https://t.me/WeebXWorld") 
                ],[
                  InlineKeyboardButton(
                        "Reports bugs and queries", url="https://t.me/Tohka_reports_bot") 
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🔴 Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📜 User Manual 📜", url="https://t.me/Tohkanews/4")
                ]
            ]
        )
   )

