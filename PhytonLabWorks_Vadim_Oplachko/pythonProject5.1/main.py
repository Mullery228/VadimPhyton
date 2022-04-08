price_list = [57.08, 46.51, 97, 28.1, 71.99, 150, 23.77, 50.5, 5, 63.18, 24.52, 95.92, 188.5, 69.99, 123.52]
print("Дефолтный список: ↓")
for i in range(len(price_list)):
    if type(price_list[i]) == float:
        str_g = str(price_list[i])
        for j in range(len(str_g) - 1):
            if str_g[j] == ".":
                str_n = str_g[j + 1:len(str_g)]
                if len(str_n) == 1:
                    str_n = str_n + "0"
        if i == len(price_list) - 1:
            print(int(price_list[i]), "руб", str_n, "коп", end="")
        else:
            print(int(price_list[i]), "руб", str_n, "коп, ", end="")
    if type(price_list[i]) == int:
        if i == len(price_list) - 1:
            print(price_list[i], "руб", "00 коп", end="")
        else:
            print(price_list[i], "руб", "00 коп, ", end="")

print("\nСортир по возрастанию: ↓")
for i in range(len(price_list) - 1):
    for j in range(len(price_list) - i - 1):
        if price_list[j] > price_list[j + 1]:
            price_list[j], price_list[j + 1] = price_list[j + 1], price_list[j]

revers_list = list(reversed(price_list))

for i in range(len(price_list)):
    if type(price_list[i]) == float:
        str_g = str(price_list[i])
        for j in range(len(str_g) - 1):
            if str_g[j] == ".":
                str_n = str_g[j + 1:len(str_g)]
                if len(str_n) == 1:
                    str_n = str_n + "0"
        if i == len(price_list) - 1:
            print(int(price_list[i]), "руб", str_n, "коп", end="")
        else:
            print(int(price_list[i]), "руб", str_n, "коп, ", end="")
    if type(price_list[i]) == int:
        if i == len(price_list) - 1:
            print(price_list[i], "руб", "00 коп", end="")
        else:
            print(price_list[i], "руб", "00 коп, ", end="")
print("\nСортир по убыванию: ↓")

for i in range(len(revers_list)):
    if type(revers_list[i]) == float:
        str_g = str(revers_list[i])
        for j in range(len(str_g) - 1):
            if str_g[j] == ".":
                str_n = str_g[j + 1:len(str_g)]
                if len(str_n) == 1:
                    str_n = str_n + "0"
        if i == len(revers_list) - 1:
            print(int(revers_list[i]), "руб", str_n, "коп", end="")
        else:
            print(int(revers_list[i]), "руб", str_n, "коп, ", end="")
    if type(revers_list[i]) == int:
        if i == len(revers_list) - 1:
            print(revers_list[i], "руб", "00 коп", end="")
        else:
            print(revers_list[i], "руб", "00 коп, ", end="")

print("\nТоп 5 цен в пятерочке: ↓")

for i in range(5):
    if type(revers_list[i]) == float:
        str_g = str(revers_list[i])
        for j in range(len(str_g) - 1):
            if str_g[j] == ".":
                str_n = str_g[j + 1:len(str_g)]
                if len(str_n) == 1:
                    str_n = str_n + "0"
        print(i + 1, ") ", int(revers_list[i]), " руб ", str_n, " коп ", sep="")
    if type(revers_list[i]) == int:
        print(i + 1, ") ", revers_list[i], " руб ", " 00 коп", sep="")

#Код можно было сократить, используя функции, но в тз не было условия с функциями
