# coding: utf-8

import os
import io

day = 4

week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
    

find_file = "ТП-27" + ".txt"
found = False
dir_ = os.listdir("data/list/")
for i in dir_:
    dir_new = os.listdir(f"data/list/{i}")
    for j in dir_new:
        if j == find_file:
            found = True
            list_ = []
            new_path = f"data/list/{i}/{find_file}"
            print(new_path)
            print(find_file)
            file_ = open(new_path, mode = "r", encoding="utf-8")
            read_file = file_.readlines()
            len_file = len(read_file)
            count = 0
            for i in range(0, len_file):
                go = read_file[i]
                if go[0] == "-":
                    print(count)
                    print("TRUE")
                    count = 0
                   
                print(go)
                print(count)
                count += 1
                   

                
            
if found == False:
    print("File is not found")
        