#-------------------------------------------------------------------------#
#------------- ИМПОРТ НЕОБХОДИМЫХ ДРЯ РАЗРАБОТКИ БИБЛИОТЕК ---------------#
#-------------------------------------------------------------------------#

import telebot
from config import *
import sys
from re import *
import sqlite3
import MySQLdb
from datetime import date
from telebot import types
from info import *
import time
import datetime

#-------------------------------------------------------------------------#

info = [] # Cписок для регистрационных данных #
timeset = [] # Список для дат


#-------------------------------------------------------------------------#
#------------------------- ОБРАБОТЧИК КОМАНД -----------------------------#
#-------------------------------------------------------------------------#
@bot.message_handler(commands = ["start"]) # обработка команды старт
def start(message):
    bot.send_message(message.chat.id , "Костанайский центр крови", reply_markup= start_select_markup) #в вывод сообщения и клавиатуры меню
def main_one(message):
    bot.send_message(message.chat.id, "Главное меню Костанайского центра крови", reply_markup= start_select_markup) #в вывод сообщения и клавиатуры меню

#-------------------------------------------------------------------------#


#-------------------------------------------------------------------------#
#-------------------ОБРАБОТЧИК ТЕКСТОВЫХ СООБЩЕНИЙ -----------------------#
#-------------------------------------------------------------------------#
@bot.message_handler(content_types = ["text"]) # обработка всех получаемых сообещний


#-------------------------------------------------------------------------#
#-----------ОБРАБОТЧИК ТЕКСТОВЫХ СООБЩЕНИЙ ОТ ГЛАВНОЙ КЛАВИАТУРЫ----------#
#-------------------------------------------------------------------------#

def main(message): # обработка сообещний получаемых от основного меню
    if message.text == "Стать донором": #условие на сообещние
        bot.send_message(message.chat.id, "Если вы хотите стать донором то, введите следующие данные") # ответ на сообещние
        msg = bot.send_message(message.chat.id, "Фамилия Имя Отчество", reply_markup=back_maprkup) # ответ на сообещние + вывод клавиатуры
        bot.register_next_step_handler(msg,input_date)     # регистрация и подготовка к исполнению следующей функции

    elif message.text == "О нас":   #условие на сообещние
        bot.send_message(message.chat.id, '*Костанайский центр крови*' + '\n'.join(aset_info[4]), parse_mode= "Markdown") # ответ на сообещние
    elif message.text == "Обратная связь":  #условие на сообещние
        msg = bot.send_message(message.chat.id, "Введите ИИН для полуучение данных о своей заявке",reply_markup=back_maprkup)# ответ на сообещние + вывод клавиатуры
        bot.register_next_step_handler(msg,send_info )  # регистрация и подготовка к исполнению следующей функции
    elif message.text == "Частые вопросы": #условие на сообещние
        msg = bot.send_message(message.chat.id, "Список частозадаваемых вопросов", reply_markup=answer_markup) # ответ на сообещние + вывод клавиатуры
    elif message.text == "Вернуться":   #условие на сообещние
        main_one(message) # переход к другой функции

#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#


#-------------------------------------------------------------------------#
#--------------ПОДКЛЮЧЕНИЕ К БД И ОТПРАВКА ДАННЫХ ПОЛЬЗОВАТЕЛЮ------------#
#-------------------------------------------------------------------------#

def send_info(message):
    if message.text == "Вернуться":
        main(message)
    else:
        iin_now = message.text
        try:                                # Данные для подключения к БД
                conn = MySQLdb.connect(
                    user="cd92325_12", 
                    password="lordfire3006",
                    port=3306,
                    host="92.53.96.20",
                    database="cd92325_12",
                    charset="utf8",
                    use_unicode=True

                )

        except MySQLdb.Error as e:           # Обработчик ошибок
            bot.send_message(message.chat.id, "Возможно данные по заявке еще не поступили или иин неверен")

        cur = conn.cursor() 
        cur.execute("SELECT * FROM users_apply WHERE iin= '%s'" % iin_now) # Делаем запрос к базе данных для сравнения введенего ИИН с существующим
        info_send = cur.fetchall()
        if not info_send: # В случае если ИИН не был найден
             bot.send_message(message.chat.id,"Данных по этому иин нет")
        else:   
            print(info_send) # В случае если ИИН был найден, то выводим все необходимые данные из БД
            for info_sends in info_send:
                bot.send_message(message.chat.id,  "Имя: {1} \n  Фамилия: {2} \n  Отчество: {3}  \n  Возраст: {4} \n  Заявка: {5} \n  Данные по заявке: {6} \n  ИИН: {7}".format(info_sends[0],info_sends[1],info_sends[2],info_sends[3],info_sends[4],info_sends[5],info_sends[6],info_sends[7]))
        conn.commit() # Заканчиваем сессию запроса
        conn.close() # Выходим из Базы ДАнных

#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#


#-------------------------------------------------------------------------#
#-----------ПОЛУЧЕНИЕ ФИО ПОЛЬЗОВАТЕЛЯ И ЗАПРОС НА ДАТУ РОЖДЕНИЯ----------#
#-------------------------------------------------------------------------#


def input_date(message):
    if message.text == "Вернуться":
        info.clear()
        timeset.clear()
        main(message)
    else:
        FIO = message.text
        info.append(FIO)
        msg = bot.send_message(message.chat.id, "Дата рождения (в формате ДД.MM.ГГГГ):")
        bot.register_next_step_handler(msg,date_check )


#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#



#-------------------------------------------------------------------------#
#-------ПРОВЕРКА ДАТЫ РОЖДЕНИЯ НА ВАЛИДНОСТЬ И НЕОБХОДИМЫЙ ВОЗРАСТ--------#
#-------------------А ТАКЖЕ ПОЛУЧЕНИЕ ЗАПРОСА НА ПОЧТУ--------------------#
#-------------------------------------------------------------------------#

def date_check(message):
    if message.text == "Вернуться":
        main(message)
        info.clear()
        timeset.clear()
    else:
        old_date = message.text
        try:
            valid_date = time.strptime(old_date, '%d.%m.%Y')
            year = valid_date.tm_year
            month = valid_date.tm_mon
            day = valid_date.tm_mday
            timeset.append(year)
            timeset.append(month)
            timeset.append(day)
            print(timeset)
            now_year = datetime.datetime.now().year
        except ValueError:
            print('Invalid date!')
            bot.send_message(message.chat.id, "Введите дату корректно корректно")
            return(input_date(message))
        if now_year - year < 18:
            bot.send_message(message.chat.id, "К сожалению вы слишком молоды для сдачи крови. Требуемый возраст не менее 18 лет")
            return(start(message))
        info.append(old_date)
        take_email(message)


def take_email(message):
        msg = bot.send_message(message.chat.id, "Ваш mail")
        bot.register_next_step_handler(msg,mail_check)

#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#


#-------------------------------------------------------------------------#
#------------ПРОВЕРКА ВАЛИДНОСТИ ВВЕДЕНОЙ ПОЛЬЗОВАТЕЛЕМ ПОЧТЫ-------------#
#-------------------А ТАКЖЕ ПОЛУЧЕНИЕ ЗАПРОСА НА ПОЛ----------------------#
#-------------------------------------------------------------------------#


def mail_check(message):
    if message.text == "Вернуться":
        info.clear()
        timeset.clear()
        main(message)
    else:
        mail = message.text
        pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
        address = mail
        is_valid = pattern.match(address)
        if is_valid:
            info.append(mail)
            bot.send_message(message.chat.id, "Выберите пол",reply_markup=select_male_markup)
        else:
            bot.send_message(message.chat.id, "Почта ввдеена не корректно")
            return(take_email(message))

#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#



#-------------------------------------------------------------------------#
#---------------------ЗАПРОС НА ВВОД ДАННЫХ О ИИН-------------------------#
#------------ПРОВЕРКА ВАЛИДНОСТИ ВВЕДЕНОГО ПОЛЬЗОВАТЕЛЕМ ИИН--------------#
#---------В СЛУЧАЕ УСПЕШНОГО ПРОХОЖДЕНИЯ ДАННЫЕ ОТПРАВЯТСЯ В БД-----------#
#-------------------------------------------------------------------------#
def take_iin(message):
        msg = bot.send_message(message.chat.id, "Ваш ИИН")
        bot.register_next_step_handler(msg,check_iin)


def check_iin(message):
    if message.text == "Вернуться":
        main(message)
        info.clear()
        timeset.clear()
    else:
        iin = message.text
        iin_two = iin
        try:
            iin = int(iin)
            print(len(iin_two))
            print(iin_two)
            print(info)
        except:
            bot.send_message(message.chat.id, "Введите иин корректно")
            return(take_iin(message))
        if len(iin_two) != 12:
            bot.send_message(message.chat.id, "Длина иин должна содержать 12 чисел")
            return(take_iin(message))
        else:
                year = timeset[0]
                month = timeset[1]
                male = info[3]
                day = timeset[2]
                new_month = int(iin_two[2] + iin_two[3])
                new_day = int(iin_two[4] + iin_two[5])
                print(day)
                print(iin_two[6])
                print(male)
                print(new_month)
                print(new_day)
                if new_month > 12 or new_month == 0 or new_month != month:
                   bot.send_message(message.chat.id,"Убедитесь в корректности иин")
                   return(take_iin(message))
                elif new_day > 31 or new_day == 0 or new_day != day:
                        bot.send_message(message.chat.id,"Убедитесь в корректности иин")
                        return(take_iin(message))
                elif iin_two[6] == "6":
                    if male == "women":
                        if year > 2001:
                            bot.send_message(message.chat.id,"Успешно")
                    else:
                        bot.send_message(message.chat.id,"Убедитесь в корректности иин")
                        return(take_iin(message))

                elif iin_two[6] == "5":
                    if male == "men":
                        if year > 2001:
                            bot.send_message(message.chat.id,"Успешно")
                        else:
                            bot.send_message(message.chat.id,"Убедитесь в корректности иин")
                            return(take_iin(message))         
                    else:
                        bot.send_message(message.chat.id,"Убедитесь в корректности иин")
                        return(take_iin(message))

                elif iin_two[6] == "4":
                    if male == "women":
                        if year < 2001:
                            bot.send_message(message.chat.id,"Успешно")
                        else:
                            bot.send_message(message.chat.id,"Убедитесь в корректности иин")
                            return(take_iin(message))  
                    else:
                        bot.send_message(message.chat.id,"Убедитесь в корректности иин")
                        return(take_iin(message))

                elif iin_two[6] == "3":
                    if male == "men":
                        if year < 2001:
                            bot.send_message(message.chat.id,"Успешно")
                        else:
                            bot.send_message(message.chat.id,"Убедитесь в корректности иин")
                            return(take_iin(message))  
                    else:
                        bot.send_message(message.chat.id,"Убедитесь в корректности иин")
                        return(take_iin(message))
        
                info.append(iin_two)
                send_to_bd(message)

#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#


#-------------------------------------------------------------------------#
#--------------ОТПРАВКА ДАННЫХ СОБРАННЫХ ОТ ПОЛЬЗОВАТЕЛЯ В БД-------------#
#-------------------------------------------------------------------------#


def send_to_bd(message):

        FIO = info[0]
        age = info[1]
        mail = info[2]
        male = info[3]
        blood_group = info[4]
        resus = info[5]
        iin = info[6]
        print(info)

        try:
            conn = MySQLdb.connect(
                    user="cd92325_12", 
                    password="lordfire3006",
                    port=3306,
                    host="92.53.96.20",
                    database="cd92325_12",
                    charset="utf8",
                    use_unicode=True

                )
            print("YES ONE")
        except:
            print("has problem")

        cur = conn.cursor()
        iin_now = iin
        cur.execute("SELECT * FROM users WHERE iin= '%s'" % iin_now)
        info_send = cur.fetchall()
        print(info_send)
        print("call")
        if not info_send:
            send =  f"INSERT INTO users(FIO, age,mail, male,blood_group, resus, iin ) VALUES ('{FIO}','{age}','{mail}','{male}','{blood_group}','{resus}','{iin}')"
            cur.execute(send)
            conn.commit()
            conn.close()
            bot.send_message(message.chat.id,"Данные успешно отправлены")
            info.clear()
            timeset.clear()
        else:
            bot.send_message(message.chat.id, "Человек с данным ИИН уже был зарегестрирован")
            conn.commit()
            conn.close()
            timeset.clear()
            info.clear()
            return(main(message))

#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#



#-------------------------------------------------------------------------#
#-------ОБРАБОТКА ВСЕХ CALLBACK ЗАПРОСОВ ОТ INLINE КЛАВИАТУРЫ-------------#
#-------------------ДЕЙСТВУЕТ В ВИДЕ ОДНОЙ ФУНКЦИИ------------------------#
#-------------------------------------------------------------------------#

@bot.callback_query_handler(func=lambda call : True)
def calling(call):
    if call.data == "1 группа крови" or call.data == "2 группа крови" or call.data == "3 группа крови" or call.data == "4 группа крови":
        blood_group = call.data
        info.append(blood_group)
        bot.send_message(call.message.chat.id, "Выберите резус фактор:", reply_markup=bload_group_select_markup)
        

    elif call.data =="Отрицательный" or call.data == "Положительный":
        resus = call.data
        info.append(resus)
        return(take_iin(call.message))

    elif call.data == "men" or call.data == "women":
        male = call.data  
        info.append(male)
        bot.send_message(call.message.chat.id, "Выберите группу крови:", reply_markup=bload_group_select_markup_two)
        
    else:
        number = int(call.data)
        bot.send_message(call.message.chat.id, '\n'.join(aset_info[number]))

#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#

bot.polling() # ЗАПУСК БОТА