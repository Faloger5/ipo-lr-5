#Доброва Анна
file = open("text.txt", "r")#открываем файл для чтения
data = file.readlines()#считываем все строки в список
new_file = open("output.txt", "w")#Открываем файл для записи
for line in data:#перебираем строки
    reversed_line = line.rstrip()[::-1]#Удаляем перенос строки и переворачиваем
    new_file.write(reversed_line + "\n")#Записываем перевёрнутую строку
