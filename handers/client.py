from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from python_bot.bot_instance import bot
from keybords import keybord

#======================HELLO====================================================================
async def hello(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Hello my master, {message.from_user.full_name}",
                           reply_markup=keybord.keyboardStat)

#======================PROBLEMS====================================================================
async def problem_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("След. задача",
                                         callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Output:"
    answer = ["0.0", '4', "0", "8", "8.0", "Error"]
    photo = open("media/problems/problem_1.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)
    await bot.send_poll(
        message.chat.id,
        question=question,
        options=answer,
        correct_option_id=0,
        is_anonymous=False,
        type="quiz",
        reply_markup=markup)


# -----------------HARRY POTTER-------------------------------------------------------------------------
async def harry_potter_1(message: types.Message):
    question = "guess the character from harry potter"
    answer = ["Christian Coulson", "Frank Bryce", "Sirius Black", "Harry Potter"]
    photo = open("media/harry_potter_character/Christian_Coulson_as_Tom_Riddle.jpg", "rb")
    markup = InlineKeyboardMarkup()
    button_harrys = InlineKeyboardButton("Следующий", callback_data="button_harrys_1")
    markup.add(button_harrys)
    await bot.send_photo(message.chat.id, photo=photo)
    await bot.send_poll(
        message.chat.id,
        question=question,
        options=answer,
        correct_option_id=1,
        is_anonymous=False,
        type="quiz",
        reply_markup=markup,
    )


#==========QUIZ=========================================================================
async def quiz_1(message: types.Message):
    question = "By whom invented Python"
    answer = ["Harry Potter", "Voldemort", "Gvido Van Rossum", "Linus Torvalds"]
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("следующий", callback_data="button_1")
    markup.add(button_1)
    await bot.send_poll(
        message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        open_period=10,
        explanation="this is easy, not gonna tell you",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


#=========CAR-QUIZ==================================================
async def car_quiz(message: types.Message):
    question = "what kind of car is this"
    answer = ["BMW M3 e46", "AUDI A6", "BMW M5 e60", "TOYOTA avensis"]
    photo = open("media/cars/bmw_m5_e60.jpg", "rb")
    markup = InlineKeyboardMarkup()
    button_car_select = InlineKeyboardButton("Следующий", callback_data="button_car_selected_1")
    markup.add(button_car_select)
    await bot.send_photo(message.chat.id, photo=photo)
    await bot.send_poll(
        message.chat.id,
        question=question,
        options=answer,
        correct_option_id=2,
        is_anonymous=False,
        type="quiz",
        reply_markup=markup,
    )



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(harry_potter_1, commands=["harry_potter"])
    dp.register_message_handler(problem_1, commands=['problem'])
    dp.register_message_handler(car_quiz, commands=["car_quiz"])