for i in range(1, 101):
    if ((i % 10 == 1) and (i != 11)):
        print(i, "процент")
    elif ((i // 10 == 1)):
        print(i, "процентов")
    elif ((i % 10 == 2) or (i % 10 == 3) or (i % 10 == 4)):
        print(i, "процента")
    elif ((i % 10 == 0) or (i % 10 == 5) or (i % 10 == 6) or (i % 10 == 7) or (i % 10 == 8) or (i % 10 == 9)):
        print(i, "процентов")