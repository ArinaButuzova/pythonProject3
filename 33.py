str_rezult = " "
str = input("Введите слово: ")

while str != "stop":
       str = input("Введите слово: ")
       str_rezult = str_rezult +str + " "

print("Результат соединения слов:", str_rezult)