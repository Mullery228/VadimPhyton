duration = int(input("Введите секунды: "))

if (duration < 60):
    print(duration, "сек")

elif ((duration >= 60) and (duration < 3600)):
    min = int (duration // 60)
    duration = duration % 60
    print(min, "мин", duration, "сек")

elif ((duration >= 3600) and (duration < 86400)):
    hour = int (duration // 3600)
    min = int ((duration % 3600)//60)
    duration = duration % 60
    print(hour, "час", min, "мин", duration, "сек")

elif (duration >= 86400):
    day = int (duration // 86400)
    hour = int ((duration // 3600) % 24)
    min = int ((duration % 3600) // 60)
    duration = duration % 60
    print(day, "дн", hour, "час", min, "мин", duration, "сек")