from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


admin_markup = InlineKeyboardMarkup()
admin_markup .add(
    InlineKeyboardButton(text = "Добавить замену", callback_data= "add_replaces")
)
admin_markup .add(
    InlineKeyboardButton(text = "Добавить обьявление", callback_data= "add_news")
)


class_select_button_one = KeyboardButton("1 курс")
class_select_button_two = KeyboardButton("2 курс")
class_select_button_three = KeyboardButton("3 курс")
class_select_button_four = KeyboardButton("4 курс")
replace = KeyboardButton("Новости")
social = KeyboardButton("КПВК в соц.сетях")

claass_select_markup = ReplyKeyboardMarkup(resize_keyboard=True)

claass_select_markup.add(
    class_select_button_one, 
    class_select_button_two,  
)
claass_select_markup.add(
    class_select_button_three, 
    class_select_button_four,
)
claass_select_markup.add(
    replace
)
claass_select_markup.add(
    social
)



social_markup = InlineKeyboardMarkup()
social_markup .add(
    InlineKeyboardButton(text = "ВКонтакте", callback_data= "VK", url="https://vk.com/club162256032")
)
social_markup .add(
    InlineKeyboardButton(text = "Instagram", callback_data= "INST", url="https://www.instagram.com/kpvk_official/")
)
social_markup .add(
    InlineKeyboardButton(text = "Facebook", callback_data= "FACEBOOK", url="https://www.facebook.com/kpvkofficial/")
)
social_markup .add(
    InlineKeyboardButton(text = "Наш сайт", callback_data= "SITE", url="https://kpvk.edu.kz/ru/")
)
social_markup .add(
    InlineKeyboardButton(text = "Youtube", callback_data= "YOUTUBE", url="https://www.youtube.com/channel/UCkDxc1hGU5pCLFaZv6j7SlA")
)



news_markup = InlineKeyboardMarkup()
        
news_markup.add(
    InlineKeyboardButton(text = "Обьявления", callback_data= "message")
)
news_markup.add(
    InlineKeyboardButton(text = "Замены", callback_data= "replaces")
)
news_markup.add(
    InlineKeyboardButton(text ="Дистанционное обучение", callback_data= "DO", url="http://185.146.0.243:8082")
)

# # KEYBOARDS FOR 1 CORUSE----------------------------------------------

# #------------------------------------------------------------------------

select_special_markup = InlineKeyboardMarkup()
        
select_special_markup.add(
    InlineKeyboardButton(text = "Информационно-экономическое", callback_data= "0")
)
select_special_markup.add(
    InlineKeyboardButton(text = "Технологическое", callback_data= "1")
)
select_special_markup.add(
    InlineKeyboardButton(text = "Электророботехническое", callback_data= "2")
)
select_special_markup.add(
    InlineKeyboardButton(text ="Механико-технологическое", callback_data= "3")
)


# #------------------------------------------------------------------------