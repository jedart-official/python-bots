import os
import telebot
import os.path
import datetime
from config import *
from markup import *
from users import*
from list_second_course import *
from list_first_course import *
from list_third_course import *
from list_four_course import *
from telebot import types
from shutil import copyfile, rmtree




def handle_docs_photo_news(message):
    try:


        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        
        downloaded_file = bot.download_file(file_info.file_path)
        roud = "news/Новости.jpg"

        src='Replaces/'+ roud
        with open(src, 'wb') as new_file:
           new_file.write(downloaded_file)
        bot.reply_to(message,"Фото добавлено",reply_markup=course_select_markup) 
        for user in joinedUsers:
            bot.send_message(user, "!! Было опубликовано обьявление !!")
    except Exception as e:
        bot.reply_to(message,e )

        
def handle_docs_photo(message):
    try:


        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        
        downloaded_file = bot.download_file(file_info.file_path)
        roud = "photos/Замена.jpg"

        src='Replaces/'+ roud
        with open(src, 'wb') as new_file:
           new_file.write(downloaded_file)
        bot.reply_to(message,"Фото добавлено",reply_markup=course_select_markup) 
        for user in joinedUsers:
            bot.send_message(user, "!! Была опубликована замена !!")

    except Exception as e:
        bot.reply_to(message,e )


def select(message):
    if message.text == "Новость":
        msg = bot.send_message(message.chat.id, "Добавьте новость", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg,handle_docs_photo_news)
    elif message.text == "Замены":
        msg = bot.send_message(message.chat.id, "Добавьте замену", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg,handle_docs_photo)




@bot.message_handler(commands = ["start"])
def start(message):
    if not str(message.chat.id) in joinedUsers:

        joinedfile = open("users.txt", "a")
        joinedfile.write(str(message.chat.id) + "\n" )
        joinedUsers.add(message.chat.id)
        
    bot.send_message(message.chat.id, "КПВК Помощник", reply_markup = course_select_markup)

@bot.message_handler(content_types=["text"])

def course_select(message):
    if message.text == "1 курс":
        bot.send_message(message.chat.id, 'Выбери отделение:', reply_markup= select_special_markup_1,parse_mode="Markdown")

    elif message.text == "2 курс":
        bot.send_message(message.chat.id, "Выбери отделение:", reply_markup= select_special_markup_2)

    elif message.text == "3 курс":
        bot.send_message(message.chat.id, "Выбери отделение:", reply_markup= select_special_markup_3)

    elif message.text == "4 курс":
        bot.send_message(message.chat.id, "Выбери отделение:", reply_markup= select_special_markup_4)

    elif message.text == "Новости":
       bot.send_message(message.chat.id, "Обьявления и новости", reply_markup= news_markup)

    elif message.text == "КПВК в соц.сетях":
       bot.send_message(message.chat.id, "Наши социальные сети", reply_markup= social_markup)
    
    elif message.text == "givemefile":
        f = open("usersInfo.txt","rb")
        bot.send_document(message.chat.id,f)

    elif message.text == "admin" or message.text == "Admin":
        msg = bot.send_message(message.chat.id, "Выберите категория для добавления", reply_markup=select_markup )
        bot.register_next_step_handler(msg,select)
    else:
        bot.send_message(message.chat.id, "Неизвестная команда, перенаправляю в главное меню...")
        return(start(message))

@bot.callback_query_handler(func=lambda call : True)

def coruse(call):
    group = ""

    if call.data == "message":
        file_list = os.listdir("Replaces/news")
        photo = open("Replaces/news/Новости.jpg", 'rb')
        bot.send_photo(call.message.chat.id, photo)

    elif call.data == "replaces":
        file_list = os.listdir("Replaces/photos")
        photo = open("Replaces/photos/Замена.jpg", 'rb')
        bot.send_photo(call.message.chat.id, photo)

#------------------------------------------------------------------------
#------------------------------------------------------------------------

    elif call.data == "1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите группу:' , reply_markup=tp_group_select_1_markup)
    
    elif call.data == "2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите группу:' , reply_markup=em_group_select_1_markup)
        
    elif call.data == "3":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите группу:' , reply_markup=tz_group_select_1_markup)

    elif call.data == "4":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите группу:' ,reply_markup=eb_group_select_1_markup)

#------------------------------------------------------------------------
#------------------------------------------------------------------------

    elif call.data == "back_1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите отделение' , reply_markup=select_special_markup_1)
    
    elif call.data == "back_2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите отделение' , reply_markup=select_special_markup_2)
   
    elif call.data == "back_3":
         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите отделение' , reply_markup=select_special_markup_3)
    
    elif call.data == "back_4":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите отделение' , reply_markup=select_special_markup_4)

#------------------------------------------------------------------------
#------------------------------------------------------------------------

    elif call.data == "2.1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите группу:' , reply_markup=tp_group_select_2_markup)

    elif call.data == "2.2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите группу:' , reply_markup=em_group_select_2_markup)
        
    elif call.data == "2.3":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите группу:' , reply_markup=tz_group_select_2_markup)
        
    elif call.data == "2.4":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите группу:' , reply_markup=eb_group_select_2_markup)

#------------------------------------------------------------------------
#------------------------------------------------------------------------

    elif call.data == "3.1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите группу:' , reply_markup=tp_group_select_3_markup)

    elif call.data == "3.2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите группу:' , reply_markup=em_group_select_3_markup)
        
    elif call.data == "3.3":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите группу:' , reply_markup=tz_group_select_3_markup)
        
    elif call.data == "3.4":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите группу:' , reply_markup=eb_group_select_3_markup)

#------------------------------------------------------------------------
#------------------------------------------------------------------------

    elif call.data == "4.1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите группу:' , reply_markup=tp_group_select_4_markup)
        
    elif call.data == "4.3":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите группу:' , reply_markup=tz_group_select_4_markup)
        
#------------------------------------------------------------------------
#------------------------------------------------------------------------
    
    try:
        now = datetime.datetime.today().weekday()
        sms = call.data
        new_sms = str(sms).replace("-", "_")
        x = globals()
        group = x[new_sms] 
   
        if now == 6:
            bot.send_message(call.message.chat.id, "Вот расписание:  " + sms)
            bot.send_message(call.message.chat.id, '\n'.join(group[0]))
        elif now == 5:
            bot.send_message(call.message.chat.id, "Вот расписание:  " + sms)
            bot.send_message(call.message.chat.id, '\n'.join(group[5]))
            bot.send_message(call.message.chat.id, '\n'.join(group[0]))

        else:
            bot.send_message(call.message.chat.id, "Вот расписание:  " + sms)
            bot.send_message(call.message.chat.id, '\n'.join(group[now]))
            bot.send_message(call.message.chat.id, '\n'.join(group[now +1]))

    except IndexError:
        print("")
    except KeyError:
        print("")

 
bot.polling()