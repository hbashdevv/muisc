from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
      await message.reply_text(
        f"""مرحبا انا {bn} 

بامكاني تشغيل الاغاني في المكالمات الجماعيه 
قم برفعي  مشرف في قناتك مع البوت المساعد [𝙎𝙉𝙀𝙆𝙍𝙎 𝙈𝙐𝙄𝙎𝘾 🍫 ⁦⁦](https://t.me/SNEKRSbot).

قم باضافتي الى مجموعتك لتبدأ الموسيقى 🎶
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⌁︙ للمساعده ︙⌁", url="https://t.me/RRPRAR")
                  ],[
                    InlineKeyboardButton(
                        "⌁︙ المـطور ︙⌁", url="https://t.me/l_IIIIIIl"
                    ),
                ],[ 
                    InlineKeyboardButton(
                        "⌁︙ اضافتي الى مجموعة ︙⌁", url="https://t.me/SNEKRSbot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(""" تم تفعيل البوت بنجاح ✅""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 مطوري ", url="https://t.me/l_IIIIIIl")
                ]
            ]
        )
   )


@Client.on_message(filters.command("panel") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(""" يمتاز هذا البوت بالبحث والتحميل ✨
اكتب معرف البوت مع اسم الاغنيه للبحث 🔊
مثال : 
@SNEKRSbot كاظم الساهر
تستطيع تحميل اي اغنيه ايضا 💞
بالاوامر التاليه :
- /ytp رابط الاغنيه من اليوتيوب
- /song رابط الاغنيه من اليوتيوب

للتحكم بالاغنية داخل المكالمه الجماعيه 🔊
- /play بالرد على الاغنيه او الرابط للتشغيل
- /pause لايقاف الاغنيه موقتا داخل المكالمه
- /resume لتكمله الاغنيه المتوقفه
- /stop لايقاف البوت عن تشغيل الاغنيه
- /skip لتخطي الاغنيه الحاليه والانتقال الى الاغنيه التاليه
#ملاحظه : تستطيع ان تقوم بتشغيل اغنيه اخرى فتضاف الى الدور بعد الاغنيه الحاليه فتتنقل بينها وبين الاغاني الباقيه باستخدام امر /skip 🔖 """,
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⌁︙ مطوري ︙⌁", url="https://t.me/l_IIIIIIl")
                ],[
                    InlineKeyboardButton(
                        "⌁︙ الحساب المساعد ︙⌁", url="https://t.me/RRPRAR"
                    )
                ]
            ]
        )
   )
