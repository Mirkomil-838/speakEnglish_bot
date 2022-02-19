from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Bu SpeakEnglish_bot 2tadan ortiq so'z yuborsangsiz en-uz tarjima qiladi. Aks holda inglizcha so'zni (inglizcha bo'lmasa tarjima qiladi) ma'nosi va o'qilishini (audiosini) yuboradi!",
            "Bu bot @Oliy_dasturchi tomonidan yaratildi")

    await message.answer("\n".join(text))
