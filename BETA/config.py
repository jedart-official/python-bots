import os
import os.path
import logging
from config import*
from markup import*
from cource_list import*
import pymysql
import datetime
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram import Dispatcher, Bot, dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import message



admin_list = ["432432432","750375616"]

class_list = {

    "1 курс" : 
    [

    #-------------FOR INFORMATIONAL and ECONOMICAL -----------------------------#

    ["ТП-28", "ТП-27", "ТП-26", "ЭБ-16", "УЭБ-2",],

    #---------------------------------Technologic-----------------------------------#

    ["ХП-20", "ХП-19",],

    #------------------------------ELECTROBOTECHNOLOGIC---------------------------------#

    ["ЭС-18", "ЭС-17", "ЭМ-7", "ЭМ-6", "Э-12"],

    #---------------------------------MEHANIC AND TECHNOLOGIC-------------------------------#

    ["ТЗ-26","ТЗ-25",]

    ], 

    "2 курс" : 
    [

    #-------------FOR INFORMATIONAL and ECONOMICAL -----------------------------#

      ["ТП-25", "ТП-24", "ТП-23", "ЭБ-15", "УЭБ-1",],

    #---------------------------------Technologic-----------------------------------#

    ["СТ-4","ХП-18", "ХП-17",],

    #------------------------------ELECTROBOTECHNOLOGIC---------------------------------#

    ["ЭС-15", "ЭС-14", "ЭМ-5", "ЭМ-4", "Э-11", "М-8"],

    #---------------------------------MEHANIC AND TECHNOLOGIC-------------------------------#

    ["ТЗ-24","ТЗ-23",]

    ],

    "3 курс" : 
    [
    #-------------FOR INFORMATIONAL and ECONOMICAL -----------------------------#

    ["ТП-22", "ТП-21", "ТП-20", "ЭБ-14",],

    #---------------------------------Technologic-----------------------------------#

    ["ХП-15", "ХП-14",],

    #------------------------------ELECTROBOTECHNOLOGIC---------------------------------#

    ["ЭС-13", "ЭС-12", "М-7", "Э-10"],

    #---------------------------------MEHANIC AND TECHNOLOGIC-------------------------------#

    ["ТЗ-22",]

    ],

    "4 курс" : 
    [

    ["ТП-19", "ТП-18", "ТП-17",],

    #------------------------------ELECTROBOTECHNOLOGIC---------------------------------#\

    ["ЭС-9",],

    ]
   

      

    

    
 
}
