# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de
# Acak-acak by @SilenceSpe4ks

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import CHANNEL, GROUP, OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>📖 ᴛᴇɴᴛᴀɴɢ ʙᴏᴛ ɪɴɪ 📖\n\n👉 ᴏᴡɴᴇʀ ʙᴏᴛ : @{OWNER}\n\n☕ ᴍᴀɴᴀɢᴇ ʙʏ : <a href='https://t.me/SilenceSpe4ks'>ᴋʟɪᴋ ᴅɪsɪɴɪ</a>\n\n🔥 sᴜᴘᴘᴏʀᴛ ʙʏ : <a href='https://t.me/SharingUserbot'>ᴋʟɪᴋ ᴅɪsɪɴɪ</a></b>\n",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [[InlineKeyboardButton("❌ 𝙏𝙐𝙏𝙐𝙋 ❌", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
