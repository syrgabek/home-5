from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from python_bot.bot_instance import bot


async def problem_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("след. задача",
                                         callback_data="button_call_2")
    markup.add(button_call_2)
    question = "Output:"
    answer = ["1", "2", "3", "4", "5", "6", "7"]
    photo = open("media/problems/problem_2.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answer,
        correct_option_id=2,
        is_anonymous=False,
        type="quiz",
        reply_markup=markup
    )


async def problem_3(call: types.CallbackQuery):
    question = "Output"
    answer = ["Error", "0", "4", "8"]
    photo = open("media/problems/problem_3.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answer,
        correct_option_id=1,
        is_anonymous=False,
        type="quiz",
    )


def register_handlers_callback_problem(dp: Dispatcher):
    dp.register_callback_query_handler(problem_2, lambda func: func.data == "button_call_1")
    dp.register_callback_query_handler(problem_3, lambda func: func.data == "button_call_2")
