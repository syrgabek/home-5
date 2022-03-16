from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from python_bot.bot_instance import bot


async def harry_potter_2(call: types.CallbackQuery):
    photo = open("media/harry_potter_character/Rubeus_Hagrid.jpg", "rb")
    question = "guess the character from harry potter"
    answers = ["Cedric Diggory", "Aberforth Dumbledore", "Rubeus Hagrid", "Dudley Dursley"]
    markup = InlineKeyboardMarkup()
    harry_button1 = InlineKeyboardButton("Следующий", callback_data="button_harrys_2")
    markup.add(harry_button1)
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        correct_option_id=2,
        is_anonymous=False,
        type="quiz",
        reply_markup=markup
    )


async def harry_poter_3(call: types.CallbackQuery):
    photo = open("media/harry_potter_character/Volan-de-Mort.jpg", "rb")
    question = "guess the character from harry potter"
    answers = ["Vernon Dursley", "Dudley Dursley", "Cedric Diggory", "Volen De Mort"]
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        correct_option_id=3,
        is_anonymous=False,
        type="quiz",
    )



def register_handlers_callback_homeWork(dp: Dispatcher):
    dp.register_callback_query_handler(harry_potter_2, lambda fun: fun.data == "button_harrys_1")
    dp.register_callback_query_handler(harry_poter_3, lambda fun: fun.data == "button_harrys_2")
