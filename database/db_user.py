import sqlite3




def sgl_create():
    global db, cursor
    db = sqlite3.connect('homework_db')
    cursor = db.cursor()
    if db:
        print('database connected successfully')
    db.execute('CREATE TABLE IF NOT EXISTS user_db '
               '(id TEXT PRIMARI KEY,username TEXT,firstname TEXT, lastname TEXT)')
    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO users_db VALUES (?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_select(message):
    for result in cursor.execute('SELECT * FROM users_db').fetchall():
        await bot.send_message(message.from_user.id,f'ID: {result[0]}\n'
                                                    f'Username: {result[1]}\n'
                                                    f'Firstname: {result[2]}\n'
                                                    f'Lastname: {result[3]}\n')



async def sql_casual_select():
    return cursor.execute('SELECT * FROM anime').fetchall()

async def sql_command_delete(data):
    cursor.execute('DELETE FROM users_db WHERE id == ?', (data,))
    db.commit()