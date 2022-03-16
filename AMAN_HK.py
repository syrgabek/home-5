from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import base, \
    InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f'Hello i am the new bot from master, if u wanna see all the commands just text /help {message.from_user.full_name}')

@dp.message_handler(commands=['help'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f'/help-- to see all commands'
                                            f'/start-- to see info about pythot'
                                            f'/quiz-- to see example quiz'
                                            f'/problem-- to see class work tasks'
                                            f'/solve_task-- to see home work from student {message.from_user.full_name}')



@dp.message_handler(commands=['quiz'])
async def poll(message: types.Message):
    question = 'By whom invented Python'
    answer = ['Harry Potter', 'Piter', 'Rate', 'Arstan']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        open_period=10,
                        explanation='You are looser',
                        explanation_parse_mode=ParseMode.MARKDOWN_V2,
                        )



@dp.message_handler(commands=['problem'])
async def problem(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('Next task',
                                         callback_data='button_call_1')
    markup.add(button_call_1)
    photo = open('../media/summfloatinteger.jpg', 'rb')
    answer1 = ['0.0', '4', '5', '8.0', 'Error']
    question1 = 'Output of this task in picture above'
    await bot.send_photo(
        message.chat.id,
        photo=photo)

    await bot.send_poll(
        message.chat.id,
        question = question1,
        options=answer1,
        correct_option_id=0,
        is_anonymous=False,
        type='quiz',
        open_period=20,
        reply_markup=markup,
        explanation = 'It is so easy so you have only 20 seconds',
        explanation_parse_mode=ParseMode.MARKDOWN_V2
    )



@dp.callback_query_handler(lambda func: func.data == 'button_call_1')
async def problem2(call: types.CallbackQuery):
    markup1 = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('Next task',
                                         callback_data='button_call_2')
    markup1.add(button_call_2)

    photo1 = open('../media/listremoveappend.jpg', 'rb')
    answer2 = ['1', '2', '3', '4', '5', '6', '7']
    question2 = 'Output of this task in picture above:'
    await bot.send_photo(
        call.message.chat.id,
        photo=photo1)
    await bot.send_poll(
        call.message.chat.id,
        question=question2,
        options=answer2,
        correct_option_id=2,
        is_anonymous=False,
        type='quiz',
        open_period=15,
        reply_markup=markup1,
        explanation='Little bit harder than previue task',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )



@dp.callback_query_handler(lambda func: func.data == 'button_call_2')
async def problem3(call: types.CallbackQuery):
    photo2 = open('../media/homework.jpg', 'rb')
    answer3 = ['0','1', '2', '3', '4', '5']
    question3 = 'Output of this task in picture above:'
    await bot.send_photo(
        call.message.chat.id,
        photo=photo2)
    await bot.send_poll(
        call.message.chat.id,
        question=question3,
        options=answer3,
        correct_option_id=0,
        is_anonymous=False,
        type='quiz',
        open_period=59,
        explanation='You can try solve this task in Pycharm',
        explanation_parse_mode=ParseMode.MARKDOWN_V2
    )


markup0 = InlineKeyboardMarkup()
button1 = InlineKeyboardButton('It is easy to me', callback_data='button1')
button2 = InlineKeyboardButton('It is so hard to me', callback_data='button2')
button3 = InlineKeyboardButton('i am tired i just wanna see the result', callback_data='button3')
button4 = InlineKeyboardButton('Tasks for lazy HUMANs', callback_data='button4')

markup0.add(button1,button2,button3,button4)

@dp.message_handler(commands=['solve_task'])
async def process_start_command(message: types.Message):
    photo_1 = open('../media/home_work_solved/task1.png', 'rb')
    await bot.send_photo(
        message.chat.id,
        photo=photo_1
    )

    await message.reply('Could you solve the task above in picture?', reply_markup=markup0)

@dp.callback_query_handler(lambda func: func.data == 'button2')
async def solved_task(call: types.CallbackQuery):
    photo4 = open('../media/home_work_solved/solvedscreen.png','rb')
    await bot.send_photo(
        call.message.chat.id,
        photo=photo4
    )

@dp.callback_query_handler(lambda func: func.data == 'button3')
async def picture(call: types.CallbackQuery):
    photo4 = open('../media/home_work_solved/picture.jpeg','rb')
    await bot.send_photo(
        call.message.chat.id,
        photo=photo4
    )

@dp.callback_query_handler(lambda func: func.data == 'button4')
async def solve_task(call: types.CallbackQuery):
    markup3 = InlineKeyboardMarkup()
    answer4 = ['0.0','1','2.0','4.0','error']
    question4 = 'Result of int2 + float2'
    button5 = InlineKeyboardButton('Next_task', callback_data='button5')
    markup3.add(button5)

    await bot.send_poll(
        call.message.chat.id,
        question=question4,
        options=answer4,
        correct_option_id=3,
        is_anonymous=False,
        type='quiz',
        explanation='only one of these options are true',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        open_period=50,
        reply_markup=markup3,
    )

@dp.callback_query_handler(lambda func: func.data == 'button5')
async def solve_task(call: types.CallbackQuery):
    answer4 = ['type error','0','1','-1','None']
    question4 = 'print((lambda x: x**2 + 5*x + 4) (-4))'
    button6 = InlineKeyboardButton('Next_task', callback_data='button6')
    markup4 = InlineKeyboardMarkup()
    markup4.add(button6)


    await bot.send_poll(
        call.message.chat.id,
        question=question4,
        options=answer4,
        correct_option_id=1,
        is_anonymous=True,
        type='quiz',
        explanation='only one of these options are true',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        open_period=50,
        reply_markup=markup4,
    )

@dp.callback_query_handler(lambda func: func.data == 'button6')
async def solve_task(call: types.CallbackQuery):
    answer4 = ['None','KeyError','0']
    question4 = 'test = {}  ' \
                'print(test[0])'

    await bot.send_poll(
        call.message.chat.id,
        question=question4,
        options=answer4,
        correct_option_id=1,
        is_anonymous=True,
        type='quiz',
        explanation='only one of these options are true',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        open_period=50,
    )

# -------------------------------------------------------------------------------


@dp.callback_query_handler(lambda func: func.data == 'button1')
async def solve_task(call: types.CallbackQuery):
    photo3 = open('../media/home_work_solved/photo5278541801109700202.jpg', 'rb')
    answer4 = ['A','B', 'C', 'All options are not correct', 'All options are correct','None']
    question4 = 'Output of this task in picture above,(WARNING, input lists have given for all task option):'

    await bot.send_photo(
        call.message.chat.id,
        photo=photo3)

    await bot.send_poll(
        call.message.chat.id,
        question=question4,
        options=answer4,
        correct_option_id=4,
        is_anonymous=False,
        type='quiz',
        explanation='only one of these options are true',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        open_period=50,
    )


@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)