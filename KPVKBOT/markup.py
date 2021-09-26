import telebot
from telebot import types

course_select_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
course_select_button_one = types.KeyboardButton("1 курс")
course_select_button_two = types.KeyboardButton("2 курс")
course_select_button_three = types.KeyboardButton("3 курс")
course_select_button_four = types.KeyboardButton("4 курс")
replace = types.KeyboardButton("Новости")
social = types.KeyboardButton("КПВК в соц.сетях")

course_select_markup.add(
    course_select_button_one, 
    course_select_button_two,  
)
course_select_markup.add(
    course_select_button_three, 
    course_select_button_four,
)
course_select_markup.add(
    replace
)
course_select_markup.add(
    social
)


select_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
select_button_one = types.KeyboardButton("Новость")
select_button_two = types.KeyboardButton("Замены")

select_markup.add(select_button_one, select_button_two)



social_markup = types.InlineKeyboardMarkup()
social_markup .add(
    types.InlineKeyboardButton(text = "ВКонтакте", callback_data= "VK", url="https://vk.com/club162256032")
)
social_markup .add(
    types.InlineKeyboardButton(text = "Instagram", callback_data= "INST", url="https://www.instagram.com/kpvk_official/")
)
social_markup .add(
    types.InlineKeyboardButton(text = "Facebook", callback_data= "FACEBOOK", url="https://www.facebook.com/kpvkofficial/")
)
social_markup .add(
    types.InlineKeyboardButton(text = "Наш сайт", callback_data= "SITE", url="https://kpvk.edu.kz/ru/")
)
social_markup .add(
    types.InlineKeyboardButton(text = "Youtube", callback_data= "YOUTUBE", url="https://www.youtube.com/channel/UCkDxc1hGU5pCLFaZv6j7SlA")
)





news_markup = types.InlineKeyboardMarkup()
        
news_markup.add(
    types.InlineKeyboardButton(text = "Обьявления", callback_data= "message")
)
news_markup.add(
    types.InlineKeyboardButton(text = "Замены", callback_data= "replaces")
)
news_markup.add(
    types.InlineKeyboardButton(text ="Дистанционное обучение", callback_data= "DO", url="http://185.146.0.243:8082")
)

# KEYBOARDS FOR 1 CORUSE----------------------------------------------

#------------------------------------------------------------------------

select_special_markup_1 = types.InlineKeyboardMarkup()
        
select_special_markup_1.add(
    types.InlineKeyboardButton(text = "Информационно-экономическое", callback_data= "1")
)
select_special_markup_1.add(
    types.InlineKeyboardButton(text = "Технологическое", callback_data= "2")
)
select_special_markup_1.add(
    types.InlineKeyboardButton(text = "Электророботехническое", callback_data= "3")
)
select_special_markup_1.add(
    types.InlineKeyboardButton(text ="Механико-технологическое", callback_data= "4")
)







#------------------------------------------------------------------------

tp_group_select_1_markup = types.InlineKeyboardMarkup()

tp_group_select_1_markup.add(
    types.InlineKeyboardButton(text ="ТП-28",callback_data= "ТП-28"), 
    types.InlineKeyboardButton(text ="ТП-27",callback_data= "ТП-27"),
)
tp_group_select_1_markup.add(
    types.InlineKeyboardButton(text ="ТП-26",callback_data= "ТП-26"), 
    types.InlineKeyboardButton(text ="ЭБ-16",callback_data= "ЭБ-16"),
)
tp_group_select_1_markup.add(
    types.InlineKeyboardButton(text ="УЭБ-2",callback_data= "УЭБ-2"),
)
tp_group_select_1_markup.add(
    types.InlineKeyboardButton(text ="Назад",callback_data= "back_1"),
)


#------------------------------------------------------------------------
#------------------------------------------------------------------------

em_group_select_1_markup = types.InlineKeyboardMarkup()

em_group_select_1_markup.add(
    types.InlineKeyboardButton( "ХП-20",callback_data= "ХП-20"),
    types.InlineKeyboardButton(text ="ХП-19",callback_data= "ХП-19"),
)
em_group_select_1_markup.add(
    types.InlineKeyboardButton(text ="Назад",callback_data= "back_1"),
)


#------------------------------------------------------------------------
#------------------------------------------------------------------------

tz_group_select_1_markup = types.InlineKeyboardMarkup()

tz_group_select_1_markup.add(
    types.InlineKeyboardButton(text ="ЭС-18",callback_data= "ЭС-18"),
    types.InlineKeyboardButton(text ="ЭС-17",callback_data= "ЭС-17"),
)
tz_group_select_1_markup.add(
    types.InlineKeyboardButton(text ="ЭМ-7",callback_data= "ЭМ-7"),
    types.InlineKeyboardButton(text ="ЭМ-6",callback_data= "ЭМ-6"),
)
tz_group_select_1_markup.add(
    types.InlineKeyboardButton(text ="Э-12",callback_data= "Э-12"),
)
tz_group_select_1_markup.add(
    types.InlineKeyboardButton(text ="Назад",callback_data= "back_1"),
)


#------------------------------------------------------------------------
#------------------------------------------------------------------------

eb_group_select_1_markup = types.InlineKeyboardMarkup()

eb_group_select_1_markup.add(
    types.InlineKeyboardButton(text ="ТЗ-26",callback_data="ТЗ-26"),
    types.InlineKeyboardButton(text ="ТЗ-25",callback_data="ТЗ-25"),
)
eb_group_select_1_markup.add(
  types.InlineKeyboardButton(text ="Назад",callback_data= "back_1"),
)



#------------------------------------------------------------------------
#------------------------------------------------------------------------


#KEYBOARDS FOR 2 CORUSE-------------------------------------------------

select_special_markup_2 = types.InlineKeyboardMarkup()
        
select_special_markup_2.add(
    types.InlineKeyboardButton(text = "Информационно-экономическое", callback_data= "2.1")
)
select_special_markup_2.add(
    types.InlineKeyboardButton(text = "Технологическое", callback_data= "2.2")
)
select_special_markup_2.add(
    types.InlineKeyboardButton(text = "Электророботехническое", callback_data= "2.3")
)
select_special_markup_2.add(
    types.InlineKeyboardButton(text ="Механико-технологическое", callback_data= "2.4")
)



#------------------------------------------------------------------------


tp_group_select_2_markup = types.InlineKeyboardMarkup()

tp_group_select_2_markup.add(
    types.InlineKeyboardButton(text ="ТП-25",callback_data= "ТП-25"), 
    types.InlineKeyboardButton(text ="ТП-24",callback_data= "ТП-24"),
)
tp_group_select_2_markup.add(
    types.InlineKeyboardButton(text ="ТП-23",callback_data= "ТП-23"), 
    types.InlineKeyboardButton(text ="ЭБ-15",callback_data= "ЭБ-15"),
)
tp_group_select_2_markup.add(
    types.InlineKeyboardButton(text ="УЭБ-1",callback_data= "УЭБ-1"),
)
tp_group_select_2_markup.add(
    types.InlineKeyboardButton(text ="Назад",callback_data= "back_2"),
)


#------------------------------------------------------------------------
#------------------------------------------------------------------------


em_group_select_2_markup = types.InlineKeyboardMarkup()

em_group_select_2_markup.add(
    types.InlineKeyboardButton( "ХП-18",callback_data= "ХП-18"),
    types.InlineKeyboardButton(text ="ХП-17",callback_data= "ХП-17"),
    
)
em_group_select_2_markup.add(
    types.InlineKeyboardButton(text ="СТ-4",callback_data= "СТ-4"),
)
em_group_select_2_markup.add(
    types.InlineKeyboardButton(text ="Назад",callback_data= "back_2"),
)

#------------------------------------------------------------------------
#------------------------------------------------------------------------

tz_group_select_2_markup = types.InlineKeyboardMarkup()

tz_group_select_2_markup.add(
    types.InlineKeyboardButton(text ="ЭС-15",callback_data= "ЭС-15"),
    types.InlineKeyboardButton(text ="ЭС-14",callback_data= "ЭС-14"),
)
tz_group_select_2_markup.add(
    types.InlineKeyboardButton(text ="ЭМ-5",callback_data= "ЭМ-5"),
    types.InlineKeyboardButton(text ="ЭМ-4",callback_data= "ЭМ-4"),
)
tz_group_select_2_markup.add(
    types.InlineKeyboardButton(text ="Э-11",callback_data= "Э-11"),
)
tz_group_select_2_markup.add(
    types.InlineKeyboardButton(text ="Назад",callback_data= "back_2"),
)


#------------------------------------------------------------------------
#------------------------------------------------------------------------


eb_group_select_2_markup = types.InlineKeyboardMarkup()

eb_group_select_2_markup.add(
    types.InlineKeyboardButton(text ="ТЗ-24",callback_data="ТЗ-24"),
    types.InlineKeyboardButton(text ="М-8",callback_data="М-8"),
)
eb_group_select_2_markup.add(
    types.InlineKeyboardButton(text ="Назад",callback_data= "back_2"),
)



#------------------------------------------------------------------------
#------------------------------------------------------------------------



#KEYBOARDS FOR 3 CORUSE-------------------------------------------------



select_special_markup_3 = types.InlineKeyboardMarkup()
        
select_special_markup_3.add(
    types.InlineKeyboardButton(text = "Информационно-экономическое", callback_data= "3.1")
)
select_special_markup_3.add(
    types.InlineKeyboardButton(text = "Технологическое", callback_data= "3.2")
)
select_special_markup_3.add(
    types.InlineKeyboardButton(text = "Электророботехническое", callback_data= "3.3")
)
select_special_markup_3.add(
    types.InlineKeyboardButton(text ="Механико-технологическое", callback_data= "3.4")
)


#------------------------------------------------------------------------



tp_group_select_3_markup = types.InlineKeyboardMarkup()

tp_group_select_3_markup.add(
    types.InlineKeyboardButton(text ="ТП-22",callback_data= "ТП-22"), 
    types.InlineKeyboardButton(text ="ТП-21",callback_data= "ТП-21"),
)
tp_group_select_3_markup.add(
    types.InlineKeyboardButton(text ="ТП-20",callback_data= "ТП-20"), 
    types.InlineKeyboardButton(text ="ЭБ-14",callback_data= "ЭБ-14"),
)
tp_group_select_3_markup.add(
    types.InlineKeyboardButton(text ="Назад",callback_data= "back_3"),
)



#------------------------------------------------------------------------
#------------------------------------------------------------------------

em_group_select_3_markup = types.InlineKeyboardMarkup()

em_group_select_3_markup.add(
    types.InlineKeyboardButton( "ХП-15",callback_data= "ХП-15"),
    types.InlineKeyboardButton(text ="ХП-14",callback_data= "ХП-14"),
)
em_group_select_3_markup.add(
    types.InlineKeyboardButton(text ="Назад",callback_data= "back_3"),
)


#------------------------------------------------------------------------
#------------------------------------------------------------------------

tz_group_select_3_markup = types.InlineKeyboardMarkup()

tz_group_select_3_markup.add(
    types.InlineKeyboardButton(text ="ЭС-13",callback_data= "ЭС-13"),
    types.InlineKeyboardButton(text ="ЭС-12",callback_data= "ЭС-12"),
)
tz_group_select_3_markup.add(
    types.InlineKeyboardButton(text ="Э-10",callback_data= "Э-10"),
)
tz_group_select_3_markup.add(
    types.InlineKeyboardButton(text ="Назад",callback_data= "back_3"),
)



#------------------------------------------------------------------------
#------------------------------------------------------------------------

eb_group_select_3_markup = types.InlineKeyboardMarkup()

eb_group_select_3_markup.add(
    types.InlineKeyboardButton(text ="ТЗ-22",callback_data="ТЗ-22"),
    types.InlineKeyboardButton(text ="М-7",callback_data="М-7"),
)
eb_group_select_3_markup.add(
    types.InlineKeyboardButton(text ="Назад",callback_data= "back_3"),
)


#------------------------------------------------------------------------
#------------------------------------------------------------------------

#KEYBOARDS FOR 4 CORUSE-------------------------------------------------

select_special_markup_4 = types.InlineKeyboardMarkup()
        
select_special_markup_4.add(
    types.InlineKeyboardButton(text = "Информационно-экономическое", callback_data= "4.1")
)

select_special_markup_4.add(
    types.InlineKeyboardButton(text = "Электророботехническое", callback_data= "4.3")
)


#------------------------------------------------------------------------

tp_group_select_4_markup = types.InlineKeyboardMarkup()

tp_group_select_4_markup.add(
    types.InlineKeyboardButton(text ="ТП-19",callback_data= "ТП-19"), 
    types.InlineKeyboardButton(text ="ТП-18",callback_data= "ТП-18"),
)
tp_group_select_4_markup.add(
    types.InlineKeyboardButton(text ="ТП-17",callback_data= "ТП-17"), 
)
tp_group_select_4_markup.add(
    types.InlineKeyboardButton(text ="Назад",callback_data= "back_4"),
)


#------------------------------------------------------------------------
#------------------------------------------------------------------------


tz_group_select_4_markup = types.InlineKeyboardMarkup()

tz_group_select_4_markup.add(
    types.InlineKeyboardButton(text ="ЭС-9",callback_data= "ЭС-9"),
)
tz_group_select_4_markup.add(
    types.InlineKeyboardButton(text ="Назад",callback_data= "back_4"),
)



#------------------------------------------------------------------------
#------------------------------------------------------------------------


