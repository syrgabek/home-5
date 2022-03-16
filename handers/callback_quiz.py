from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from python_bot.bot_instance import bot


async def quiz_2(call: types.CallbackQuery):
    question = "what year was the python invented?"
    answer = ["1980", "1999", "1991", "2000"]
    markup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton("следующий", callback_data="button_2")
    markup.add(button_2)
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        open_period=10,
        explanation="Распад СССР",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    question = "what is python based on"
    answer = ["C", "Java", "JavaScript", "assambler"]
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type="quiz",
        correct_option_id=0,
        open_period=10,
        explanation="Father C++",
        explanation_parse_mode=ParseMode.MARKDOWN_V2
    )


def register_handler_callback_quiz(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda fun: fun.data == "button_1")
    dp.register_callback_query_handler(quiz_3, lambda fun: fun.data == "button_2")
