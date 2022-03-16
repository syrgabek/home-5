from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from python_bot.bot_instance import bot


async def answer_yes(call: types.CallbackQuery):
    photo = open("media/home_work_images/answers.jpg", "rd")
    question = "Угадай ..."
    answers = ["A", "B", "C"]
    markup = InlineKeyboardMarkup()
    button_a = InlineKeyboardButton("A", callback_data="button_a")
    button_b = InlineKeyboardButton("B", callback_data="button_b")
    button_c = InlineKeyboardButton("C", callback_data="button_c")
    markup.add(button_a, button_b, button_c)
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        correct_option_id=0,
        reply_markup=markup
    )


async def answer_no(call: types.CallbackQuery):
    photo = open("media/home_work_images/home_work_perf.jpg", "rd")
    await bot.send_photo(call.message.chat.id, photo=photo)


def register_handlers_callback_homeWork(dp: Dispatcher):
    dp.register_callback_query_handler(answer_yes, lambda fun: fun.data == "button_yes")
    dp.register_callback_query_handler(answer_no, lambda fun: fun.data == "button_no")