#Доброва Анна
file_ = "S:/students/GR_88/Доброва Анна/ИПО/text.txt"#путь файла
with open(file_, 'r') as file:#открываем файл для чтения
    data = file.read()#чтение файла
    words = data.split()#разбивает на слова по пробелам
print ("Кол-во слов в файле: ", len(words))#вывод результата
