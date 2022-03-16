from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from python_bot.bot_instance import bot


class FSMADMIN(StatesGroup):
    id = State()
    username = State()
    first_name = State()
    last_name = State()


async def get_user_id(message: types.Message):
    global USER_ID
    USER_ID = message.from_user.id
    await bot.send_message(message.from_user.id, "User, what do u need")


async def fsm_start(message: types.Message):
    if message.from_user.id == USER_ID:
        await FSMADMIN.id.set()
        await message.reply("Enter username")


async def load_username(message: types.Message,
                        state: FSMContext):
    if message.from_user.id == USER_ID:
        async with state.proxy() as data:
            data["username"] = message.photo[0].file_id
        await FSMADMIN.next()
        await message.reply("Enter first_name")


async def load_first_name(message: types.Message,
                          state: FSMContext):
    if message.from_user.id == USER_ID:
        async with state.proxy() as data:
            data["first_name"] = message.text
        await FSMADMIN.next()
        await message.reply("Enter last_name")


async def load_last_name(message: types.Message,
                         state: FSMContext):
    if message.from_user.id == USER_ID:
        async with state.proxy() as data:
            data["last_name"] = message.text
        async with state.proxy() as data:
            await message.reply(str(data))
        await state.finish()


def register_handler_fsmadmin(dp: Dispatcher):

    dp.register_message_handler(fsm_start, commands=["dsa"], state=None)
    dp.register_message_handler(load_username,  state=FSMADMIN.username)
    dp.register_message_handler(load_first_name,  state=FSMADMIN.first_name)
    dp.register_message_handler(load_last_name,  state=FSMADMIN.last_name)
    dp.register_message_handler(get_user_id,commands=['user_registor'],get_user_id=True)
