
from os import name

from config import *
from markup import *
from cource_list import *

from aiogram.dispatcher.storage import FSMContext
from aiogram.types import message
from aiohttp.hdrs import CONTENT_TYPE
from aiogram import Dispatcher, bot, dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import datetime
import logging
import pymysql

bot = Bot(token="1867595092:AAE2G7LpMuno9EoOCoOxqM6qa0zjp1PnV-o")
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

class select_cource(StatesGroup):
    course = State()




@dp.callback_query_handler(lambda c: c.data == "add_replaces",state= None)
async def cource_select(callback_query: types.CallbackQuery):
    await bot.send_message(
        chat_id= callback_query.message.chat.id,
        text = "Выберите курс обучения"
    )





class replace_apply(StatesGroup):
    add_replaces_1 = State()
    add_replaces_2 = State()

class news_apply(StatesGroup):
    news_1 = State()
    news_2 = State()


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    user_ids = str(message.from_user.id)
    
    
    try:  # Данные для подключения к БД
        conn = pymysql.connect(
            user="cd92325_bot",
            password="Qwerty3005",
            port=3306,
            host="92.53.96.20",
            database="cd92325_bot",
            charset="utf8",
            use_unicode=True

        )

    except pymysql.Error as e:  # Обработчик ошибок
        await bot.send_message(
            chat_id = message.chat.id,
            text = "Ошибка подключения к базе данных"
        )

    cur = conn.cursor()
    info = cur.execute(f'SELECT * FROM users WHERE user_id={user_ids}')
    info = cur.fetchall()
    if not info:
        send = f"INSERT INTO users(user_id, name, surname, username) VALUES ('{message.from_user.id}','{message.from_user.first_name}','{message.from_user.last_name}','{message.from_user.username}')"
        cur.execute(send)  # Делаем запрос к базе данных для сравнения введенего ИИН с существующим
    conn.commit()  # Заканчиваем сессию запроса
    conn.close()  # Выходим из Базы ДАнных

    if user_ids in admin_list:
        await message.answer("КПВК Помощник", reply_markup=adminMarkup)
    if user_ids not in admin_list:
        await message.answer("КПВК Помощник", reply_markup=course_select_markup)

@dp.message_handler()
async def course_select(message):
    user_id = str(message.from_user.id)
    if message.text == "1 курс":
        await message.answer('Выбери отделение:', reply_markup=select_special_markup_1, parse_mode="Markdown")

    elif message.text == "2 курс":
        await message.answer("Выбери отделение:", reply_markup=select_special_markup_2)

    elif message.text == "3 курс":
        await message.answer("Выбери отделение:", reply_markup=select_special_markup_3)

    elif message.text == "4 курс":
        await message.answer("Выбери отделение:", reply_markup=select_special_markup_4)

    elif message.text == "Новости":
        await message.answer("Обьявления и новости", reply_markup=news_markup)

    elif message.text == "КПВК в соц.сетях":
        await message.answer("Наши социальные сети", reply_markup=social_markup)

    elif message.text == "Админ панель":
        if user_id in admin_list:
            await message.answer("Админ панель", reply_markup=admin_markup)
        if user_id not in admin_list:
            await message.answer("У вас нет прав жля исполнения данной команды")

# @dp.callback_query_handler(lambda c: c.data == "add_replaces", state=None)
# async def add_replaces(callback_query: types.CallbackQuery):
#     await  bot.send_message(callback_query.message.chat.id, "Добавьте замену")
#     await  replace_apply.add_replaces_1.set()

# @dp.message_handler(state=replace_apply.add_replaces_1, content_types=message.ContentType.PHOTO)
# async def add_replaces_2(message, state=FSMContext):
    # try:
    #     file_info = await bot.get_file(message.photo[len(message.photo) - 1].file_id)
    #     downloaded_file = await bot.download_file(file_info.file_path)
    #     roud = "photos/Замена.jpg"

    #     src = 'Replaces/' + roud
    #     with open(src, 'wb') as new_file:
    #         new_file.write(downloaded_file.getvalue())
    #     await message.answer("Фото добавлено")
    #     await state.finish()

    # except Exception as e:
    #     await bot.send_message(
    #         chat_id = message.chat.id,
    #         text = "Во время добавления замены возникла ошибка"
    #     )

    # try:  # Данные для подключения к БД
    #     conn = pymysql.connect(
    #         user="cd92325_bot",
    #         password="Qwerty3005",
    #         port=3306,
    #         host="92.53.96.20",
    #         database="cd92325_bot",
    #         charset="utf8",
    #         use_unicode=True

    #     )

    # except pymysql.Error as e:  # Обработчик ошибок
    #     print("rjczr")

    # cur = conn.cursor()
    # info = cur.execute("SELECT * FROM users")
    # info = list(cur.fetchall())
    # print(info[0])
    # for i in info:
    #     await bot.send_message( chat_id= i[1], text= "Была опубликована запись")
    # conn.commit()  # Заканчиваем сессию запроса
    # conn.close()  # Выходим из Базы ДАнных

@dp.callback_query_handler(lambda c: c.data == "add_news", state=None)
async def add_replaces(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.message.chat.id, "Добавьте обьявление")
    await news_apply.news_1.set()

@dp.message_handler(state=news_apply.news_1, content_types=message.ContentType.PHOTO)
async def add_replaces_2(message, state=FSMContext):
    try:
        file_info = await bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = await bot.download_file(file_info.file_path)
        roud = "news/Новости.jpg"
        src = 'Replaces/' + roud
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file.getvalue())
        await message.answer("Фото добавлено")
        await state.finish()

    except Exception as e:
        await bot.send_message(
            chat_id = message.chat.id,
            text = "Во время добавления новости возникла ошибка"
        )

    try:  # Данные для подключения к БД
        conn = pymysql.connect(
            user="cd92325_bot",
            password="Qwerty3005",
            port=3306,
            host="92.53.96.20",
            database="cd92325_bot",
            charset="utf8",
            use_unicode=True

        )

    except pymysql.Error as e:  # Обработчик ошибок
        await bot.send_message(
            chat_id = message.chat.id,
            text = "Ошибка подключения к базе данных"
        )

    cur = conn.cursor()
    info = cur.execute("SELECT * FROM users")
    info = list(cur.fetchall())
    for i in info:
        await bot.send_message( chat_id= i[1], text= "Была опубликована запись")
    conn.commit()  # Заканчиваем сессию запроса
    conn.close()  # Выходим из Базы ДАнных


@dp.callback_query_handler(lambda callback_query: True)
async def coruse(callback_query: types.CallbackQuery):
    callback_data = callback_query.data

    if callback_data == "message":
        photo = open("Replaces/news/Новости.jpg", 'rb')
        await bot.send_photo(callback_query.message.chat.id, photo)

    elif callback_data == "replaces":
        photo = open("Replaces/photos/Замена.jpg", 'rb')
        await bot.send_photo(callback_query.message.chat.id, photo)


    elif callback_data == "1":
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id, text='Выберите группу:',
                                    reply_markup=tp_group_select_1_markup)

    elif callback_data == "2":
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id, text='Выберите группу:',
                                    reply_markup=em_group_select_1_markup)

    elif callback_data == "3":
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id, text='Выберите группу:',
                                    reply_markup=tz_group_select_1_markup)

    elif callback_data == "4":
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id, text='Выберите группу:',
                                    reply_markup=eb_group_select_1_markup)

    elif callback_data == "back_1":
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id, text='Выберите отделение',
                                    reply_markup=select_special_markup_1)

    elif callback_data == "back_2":
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id, text='Выберите отделение',
                                    reply_markup=select_special_markup_2)

    elif callback_data == "back_3":
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id, text='Выберите отделение',
                                    reply_markup=select_special_markup_3)

    elif callback_data == "back_4":
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id, text='Выберите отделение',
                                    reply_markup=select_special_markup_4)

    elif callback_data == "2.1":
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id, text='Выберите группу:',
                                    reply_markup=tp_group_select_2_markup)

    elif callback_data == "2.2":
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id, text='Выберите группу:',
                                    reply_markup=em_group_select_2_markup)

    elif callback_data == "2.3":
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id, text='Выберите группу:',
                                    reply_markup=tz_group_select_2_markup)

    elif callback_data == "2.4":
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id, text='Выберите группу:',
                                    reply_markup=eb_group_select_2_markup)

    elif callback_data == "3.1":
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id, text='Выберите группу:',
                                    reply_markup=tp_group_select_3_markup)

    elif callback_data == "3.2":
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id, text='Выберите группу:',
                                    reply_markup=em_group_select_3_markup)

    elif callback_data == "3.3":
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id, text='Выберите группу:',
                                    reply_markup=tz_group_select_3_markup)

    elif callback_data == "3.4":
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id, text='Выберите группу:',
                                    reply_markup=eb_group_select_3_markup)

    elif callback_data == "4.1":
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id, text='Выберите группу:',
                                    reply_markup=tp_group_select_4_markup)

    elif callback_data == "4.3":
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id, text='Выберите группу:',
                                    reply_markup=tz_group_select_4_markup)

    else:
        now = datetime.datetime.today().weekday()
        sms = str(callback_data).replace("-", "_")
        if now == 6:
            await bot.send_message(callback_query.message.chat.id, "Вот расписание:  " + callback_data)
            await bot.send_message(callback_query.message.chat.id, '\n'.join(first_course_list[sms][0]))
        elif now == 5:
            await bot.send_message(callback_query.message.chat.id, "Вот расписание:  " + callback_data)
            await bot.send_message(callback_query.message.chat.id, '\n'.join(first_course_list[sms][5]))
            await bot.send_message(callback_query.message.chat.id, '\n'.join(first_course_list[sms][0]))

        else:
            await bot.send_message(callback_query.message.chat.id, "Вот расписание:  " + callback_data)
            await bot.send_message(callback_query.message.chat.id, '\n'.join(first_course_list[sms][now]))
            await bot.send_message(callback_query.message.chat.id, '\n'.join(first_course_list[sms][now + 1]))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
