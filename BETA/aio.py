from config import *

bot = Bot(token="1867595092:AAE2G7LpMuno9EoOCoOxqM6qa0zjp1PnV-o")
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


class replace_apply(StatesGroup):
    add_replaces_step_first = State()
    add_replaces_step_second = State()

class news_apply(StatesGroup):
    news_step_first = State()
    news_step_second = State()

@dp.message_handler(commands=["start"] , state= None)
async def start(message: types.Message):
    users_id = str(message.from_user.id)
    
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
    info = cur.execute(f'SELECT * FROM users WHERE user_id={users_id}')
    info = cur.fetchall()
    if not info:
        send = f"INSERT INTO users(user_id, name, surname, username) VALUES ('{message.from_user.id}','{message.from_user.first_name}','{message.from_user.last_name}','{message.from_user.username}')"
        cur.execute(send)  # Делаем запрос к базе данных для сравнения введенего ИИН с существующим
    conn.commit()  # Заканчиваем сессию запроса
    conn.close()  # Выходим из Базы ДАнных

    if users_id in admin_list:
        admin_button = KeyboardButton(text = "Админ панель")
        claass_select_markup.add(admin_button)
        await message.answer("КПВК Помощник", reply_markup=claass_select_markup)
    if users_id not in admin_list:
        await message.answer("КПВК Помощник", reply_markup=claass_select_markup)
    

@dp.message_handler()
async def course_select(message, state = FSMContext):
    await state.update_data(cource = message.text)
    user_id = str(message.from_user.id)
    if message.text == "1 курс" or message.text == "2 курс" or message.text == "3 курс" or message.text == "4 курс":
        await message.answer('Выбери отделение:', reply_markup=select_special_markup, parse_mode="Markdown")

    elif message.text == "Новости":
        await message.answer("Обьявления и новости", reply_markup=news_markup)

    elif message.text == "КПВК в соц.сетях":
        await message.answer("Наши социальные сети", reply_markup=social_markup)

    elif message.text == "Админ панель":
        if user_id in admin_list:
            await message.answer("Админ панель", reply_markup=admin_markup)
        if user_id not in admin_list:
            await message.answer("У вас нет прав жля исполнения данной команды")


@dp.callback_query_handler(lambda c: c.data == "add_replaces", state = None)
async def add_replaces(callback_query: types.CallbackQuery):
    await  bot.send_message(callback_query.message.chat.id, "Добавьте замену")
    await  replace_apply.add_replaces_step_first.set()

@dp.message_handler(state = replace_apply.add_replaces_step_first, content_types = message.ContentType.PHOTO)
async def add_replaces_2(message, state = FSMContext):
    try:
        file_info = await bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = await bot.download_file(file_info.file_path)
        way = "photos/Замена.jpg"
        src = 'Replaces/' + way
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file.getvalue())
        await message.answer("Фото добавлено")
        await state.finish()

    except Exception:
        await bot.send_message(
            chat_id = message.chat.id,
            text = "Во время добавления замены возникла ошибка"
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
        print("rjczr")

    cur = conn.cursor()
    info = cur.execute("SELECT * FROM users")
    info = list(cur.fetchall())
    print(info[0])
    for i in info:
        await bot.send_message( chat_id= i[1], text= "Была опубликована запись")
    conn.commit()  # Заканчиваем сессию запроса
    conn.close()  # Выходим из Базы ДАнных

@dp.callback_query_handler(lambda c: c.data == "add_news", state = None)
async def add_replaces(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.message.chat.id, "Добавьте обьявление")
    await news_apply.news_step_first.set()

@dp.message_handler(state = news_apply.news_step_first, content_types = message.ContentType.PHOTO)
async def add_replaces_2(message, state = FSMContext):
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
async def class_select(callback_query: types.CallbackQuery, state = FSMContext):
    callback_data = callback_query.data

    if callback_data == "message":
        photo = open("Replaces/news/Новости.jpg", 'rb')
        await bot.send_photo(callback_query.message.chat.id, photo)

    elif callback_data == "replaces":
        photo = open("Replaces/photos/Замена.jpg", 'rb')
        await bot.send_photo(callback_query.message.chat.id, photo)

    elif callback_data == "0" or callback_data == "1" or callback_data == "2" or callback_data == "3":
        special_number = int(callback_data)
        cource = await state.get_data()
        cource = cource['cource']
        cource_markup = InlineKeyboardMarkup()
        for i in class_list[cource][special_number]:
            cource_markup.add(
                InlineKeyboardButton(text = i, callback_data= f"{i}")
        )
        cource_markup.add(
            InlineKeyboardButton(text = "Вернуться", callback_data= "back")
        )

        await bot.edit_message_text(
            text = "Выберите группы",
            chat_id= callback_query.message.chat.id,
            message_id= callback_query.message.message_id,
            reply_markup= cource_markup
        )
             
    elif callback_data == "back":
        await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id, text='Выберите отделение',
            reply_markup=select_special_markup
        )

    else:
        now = datetime.datetime.today().weekday()
        group = str(callback_data).replace("-", "_")
        if now == 6:
            await bot.send_message(callback_query.message.chat.id, "Вот расписание:  " + callback_data)
            await bot.send_message(callback_query.message.chat.id, '\n'.join(class_text_list[group][0]))
        elif now == 5:
            await bot.send_message(callback_query.message.chat.id, "Вот расписание:  " + callback_data)
            await bot.send_message(callback_query.message.chat.id, '\n'.join(class_text_list[group][5]))
            await bot.send_message(callback_query.message.chat.id, '\n'.join(class_text_list[group][0]))

        else:
            await bot.send_message(callback_query.message.chat.id, "Вот расписание:  " + callback_data)
            await bot.send_message(callback_query.message.chat.id, '\n'.join(class_text_list[group][now]))
            await bot.send_message(callback_query.message.chat.id, '\n'.join(class_text_list[group][now + 1]))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)