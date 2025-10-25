#Доброва Анна
file_ = "S:/students/GR_88/Доброва Анна/ИПО/text.txt" #путь файла
with open(file_, 'r', encoding ='utf-8') as file:#открываем файл для чтения
    data = file.readlines()#чтение файла
new_file = "S:/students/GR_88/Доброва Анна/ИПО/output.txt" #путь файла
with open(new_file, "w",  encoding ='utf-8') as file:#Открываем файл для записи
    for line in data:#перебираем строки
        reversed_line = line.rstrip()[::-1]#Удаляем перенос строки и переворачиваем
        file.write(reversed_line + "\n")#Записываем перевёрнутую строку

