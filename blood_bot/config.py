#-------------------------------------------------------------------------#
#------------- ИМПОРТ НЕОБХОДИМЫХ ДРЯ РАЗРАБОТКИ БИБЛИОТЕК ---------------#
#-------------------------------------------------------------------------#
import telebot
from telebot import types

#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#



#-------------------------------------------------------------------------#
#----------------------------ИМПОРТ ТОКЕНА--------------------------------#
#-------------------------------------------------------------------------#

TOKEN = "1229205188:AAFlyN1XOzFmqrcs9dhcswGn-sxO3sRfOyY"
bot = telebot.TeleBot(TOKEN)
#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#




#-------------------------------------------------------------------------#
#----------------------ОСНОВНАЯ КЛАВИАТУРА БОТА---------------------------#
#-------------------------------------------------------------------------#

start_select_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
about_us_button = types.KeyboardButton("О нас")
apply_button = types.KeyboardButton("Стать донором")
feedback = types.KeyboardButton("Обратная связь")
ans_questions=types.KeyboardButton("Частые вопросы")

start_select_markup.add(about_us_button, apply_button, feedback,ans_questions)
#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#


#-------------------------------------------------------------------------#
#----------------КЛАВИАТУРА ДЛЯ ОТВЕТОВ НА ЧАСТЫЕ ВПОРОСЫ-----------------#
#-------------------------------------------------------------------------#

answer_markup = types.InlineKeyboardMarkup()

answer_markup.add(
     types.InlineKeyboardButton(text = "Порядок приема безвозмездных доноров:", callback_data="0"),
)
answer_markup.add(
     types.InlineKeyboardButton(text = "Питание доноров", callback_data="1"),
)
answer_markup.add(
     types.InlineKeyboardButton(text = "Безопасность донорства", callback_data="2"),
)
answer_markup.add(
     types.InlineKeyboardButton(text = "Прием доноров", callback_data="3"),
)

#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#

back_maprkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_maprkup.add(
    types.KeyboardButton("Вернуться")
)

#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#



#-------------------------------------------------------------------------#
#--------------КЛАВИАТУРА ВЫБОРА ГРУПП КРОВИ И РЕЗУС ФАКТОРА--------------#
#-------------------------------------------------------------------------#

bload_group_select_markup = types.InlineKeyboardMarkup()
bload_group_select_markup.add(
    types.InlineKeyboardButton(text = "Отрицательный", callback_data="Отрицательный"),
    
)
bload_group_select_markup.add(
    types.InlineKeyboardButton(text = "Положительный", callback_data="Положительный")
)

bload_group_select_markup_two = types.InlineKeyboardMarkup()
bload_group_select_markup_two.add(
    types.InlineKeyboardButton(text = "1 группа крови", callback_data="1 группа крови")
)
bload_group_select_markup_two.add(
    types.InlineKeyboardButton(text = "2 группа крови", callback_data="2 группа крови")
)
bload_group_select_markup_two.add(
    types.InlineKeyboardButton(text = "3 группа крови", callback_data="3 группа крови")
)
bload_group_select_markup_two.add(
    types.InlineKeyboardButton(text = "4 группа крови", callback_data="4 группа крови")
)



#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#

#-------------------------------------------------------------------------#
#--------------КЛАВИАТУРА ВЫБОРА ПОЛА(МУЖСКОГО ИЛИ ЖЕНСКОГО---------------#
#-------------------------------------------------------------------------#
select_male_markup = types.InlineKeyboardMarkup()
select_male_markup.add(
    types.InlineKeyboardButton(text = "Мужской", callback_data="men")
)
select_male_markup.add(
    types.InlineKeyboardButton(text = "Женский", callback_data="women")
)


#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#