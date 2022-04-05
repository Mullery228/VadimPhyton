list = [i for i in range(1, 1000, 2)]
print("Изначальный список ->", list)
for i in range(len(list)):
    list[i] = list[i] ** 3
print("Список кубов ->", list)
print("Числа, которые соответствуют заданному условию ↓")
for i in range(len(list)):
    sum = 0
    copy = list[i]
    while (list[i] != 0):
        sum = sum + list[i] % 10
        list[i] = list[i] // 10
        if((sum % 7 == 0) and (list[i] == 0)):
            print(copy)
    list[i] = copy

print("Тут добавили 17 к кубам и еще раз проверили на условие ↓")
for i in range(len(list)):
    list[i] = list[i] + 17
    sum = 0
    copy = list[i]
    while (list[i] != 0):
        sum = sum + list[i] % 10
        list[i] = list[i] // 10
        if((sum % 7 == 0) and (list[i] == 0)):
            print(copy)