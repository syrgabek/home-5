from aiogram import executor
from python_bot.bot_instance import dp
from handers import client, extra ,callback_quiz, callback_problem, callback_home_work, callback_quizColor, callback_harry_potter, fsmadmin

fsmadmin.register_handler_fsmadmin(dp)
client.register_handlers_client(dp)
callback_quiz.register_handler_callback_quiz(dp)
callback_problem.register_handlers_callback_problem(dp)
callback_home_work.register_handlers_callback_homeWork(dp)
callback_quizCars.register_handlers_callback_homeWork(dp)
callback_harry_potter.register_handlers_callback_homeWork(dp)
extra.register_handlers_extra(dp)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
