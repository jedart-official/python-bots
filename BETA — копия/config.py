import os
import os.path
import logging
from config import*
from aiogram import Dispatcher, Bot, dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


admin_list = ["432432432","750375616"]

first_list = [
    #-------------FOR INFORMATIONAL and ECONOMICAL -----------------------------#
    ["ТП-28", "ТП-27", "ТП-26", "ЭБ-16", "УЭБ-2",],
    #---------------------------------Technologic-----------------------------------#
    ["ХП-20", "ХП-19",],
    #------------------------------ELECTROBOTECHNOLOGIC---------------------------------#
    ["ЭС-18", "ЭС-17", "ЭМ-7", "ЭМ-6", "Э-12"],
    #---------------------------------MEHANIC AND TECHNOLOGIC-------------------------------#
    ["ТЗ-26","ТЗ-25",]

]
