name_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
str_name = str()
for i in range(len(name_list)):
    str_general = str(name_list[i])
    for j in range(len(str_general) - 1, 0, -1):
        if str_general[j] == " ":
            str_name = str_general[j + 1 : len(str_general)]
            break
    str_name = str_name.lower() #приводим все буквы в одинаковый формат, что потом заглавить первую
    print("Привет, ", str_name.capitalize(), "!", sep="")