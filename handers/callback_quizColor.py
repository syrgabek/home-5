from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from python_bot.bot_instance import bot


async def color_select_2(call: types.CallbackQuery):
    photo = open("media/color/red.jpg", "rb")
    question = "what color is this"
    answers = ["red", "blue", "grey", "pink"]
    markup = InlineKeyboardMarkup()
    button_car = InlineKeyboardButton("Следующий", callback_data="button_color_selected_2")
    markup.add(button_car)
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        correct_option_id=1,
        is_anonymous=False,
        type="quiz",
        reply_markup=markup
    )


async def color_select_3(call: types.CallbackQuery):
    photo = open("media/color/black.jpg", "rb")
    question = "what color is this"
    answers = ["black", "green", "orage", "red"]
    markup = InlineKeyboardMarkup()
    button_car2 = InlineKeyboardButton("Следующий", callback_data="button_car_selected_3")
    markup.add(button_car2)
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


async def color_select_4(call: types.CallbackQuery):
    photo = open("media/color/gold.jpg", "rb")
    question = "what clor is this"
    answers = ["gold", "silver", "azure", "pearl"]
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        correct_option_id=3,
        is_anonymous=False,
        type="quiz"
    )


def register_handlers_callback_homeWork(dp: Dispatcher):
    dp.register_callback_query_handler(color_select_2, lambda fun: fun.data == "button_color_selected_1")
    dp.register_callback_query_handler(color_select_3, lambda fun: fun.data == "button_color_selected_2")
    dp.register_callback_query_handler(color_select_4(), lambda fun: fun.data == "button_color_selected_3")
