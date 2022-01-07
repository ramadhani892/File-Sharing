# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de
# Acak-acak by @SilenceSpe4ks

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import OWNER_ID


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>👑 Owner : <a href='tg://user?id={OWNER_ID}'>Klik Disini</a>\n\n☕ Managed By : <a href='https://t.me/SilenceSpe4ks'>Klik Disini</a>\n\n🔥 Source Code : <a href='https://github.com/zigaz23'>Klik Disini</a></b>\n",
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
