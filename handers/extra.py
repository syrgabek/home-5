from aiogram import types, Dispatcher
from python_bot.bot_instance import bot


async def secret_word(message: types.Message):
    await message.reply("yes my master")

async def ban(message: types.Message):
    ban_words = ['java', 'bitch', 'slut', 'python is bad']
    for i in ban_words:
        if i in message.text.lower().replace(" ", ""):
            await message.delete()
            await bot.send_message(message.chat.id, "Bot-Admin deleted bad words")
    if message.text.lower() == "dice":
        await bot.send_dice(message.chat.id, emoji="🎲")
    elif message.text.startswith("pin"):
        await bot.pin_chat_message(message.chat.id, message.message_id)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(secret_word, lambda word: "dorei" in word.text)
    dp.register_message_handler(ban, content_types=['text'])