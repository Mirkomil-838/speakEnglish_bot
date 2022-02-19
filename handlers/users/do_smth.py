from oxfordLookup import getDefinitions
from translate import translate, language
from aiogram import types
from loader import dp

@dp.message_handler()
async def do_smth(message: types.Message):
    if len(message.text.split()) > 2:
        dest = 'en'
        lang = language(message.text)
        if lang == 'en':
            dest = 'uz'  
        else:
            dest = 'en'
        await message.reply(translate(message.text, dest))

    else:
        mes = translate(message.text)
        dest = 'uz'
        if language(message.text) != 'en':
            dest = 'en'
        if getDefinitions(mes):
            data = getDefinitions(mes)
            await message.reply(f"{message.text} - {translate(message.text, dest)} \n{data['definitions']}")
            if data.get('audioFile'):
                await message.answer_voice(data['audioFile'])

        else:
            dest = 'en'
            lang = language(message.text)
            if lang == 'en':
                dest = 'uz'  
            else:
                dest = 'en'
            await message.reply(translate(message.text, dest))
            # await message.reply('Bunday ma\'lumot topilmadi')
