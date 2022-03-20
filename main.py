from aiogram import executor
from bot_instance import dp
from handers import client, callback, extra
from database import bot_db,db_user
from handers import fsmadmin

async def on_startup(_):
    bot_db.sql_create()
    db_user.sql_create()

fsmadmin.register_handler_fsm_admin_user(dp)
fsmadmin.register_handler_fsmadmin(dp)
client.refister_handlers_cilent(dp)
callback.register_handlers_callback(dp)
extra.register_handler_extra(dp)




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
