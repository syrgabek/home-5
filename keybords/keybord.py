from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_quiz = KeyboardButton("/quiz")
button_problem = KeyboardButton("/problem")
button_harry_potter = KeyboardButton("/harry_potter")
button_car_quiz = KeyboardButton("/car_quiz")
button_location = KeyboardButton("Share location", request_location=True)
button_info = KeyboardButton("Share info", request_contact=True)

keyboardStat = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4, one_time_keyboard=True)
keyboardStat.add(button_quiz, button_problem, button_harry_potter, button_car_quiz,button_location, button_info)