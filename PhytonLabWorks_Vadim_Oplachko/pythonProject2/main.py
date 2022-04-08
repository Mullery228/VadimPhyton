some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(some_list)
for i in range(len(some_list) - 1, 0, -1):
    if some_list[i].isdigit() == True and len(some_list[i]) == 1: #условие для выявления однозначных чисел в списке строк
        some_list.insert(i, '"')
        some_list.insert(i + 2, '"')
        some_list[i + 1] = "0" + some_list[i + 1]
    if some_list[i].isdigit() == True: #условие для двузначных чисел
        some_list.insert(i, '"')
        some_list.insert(i + 2, '"')
    if some_list[i].find("+") != -1: #условие для чисел со знаком +
        str_ = some_list[i]
        some_list.insert(i, '"')
        some_list.insert(i + 2, '"')
        str_ = str_[:1], '0', str_[1:] #тут на выходе получается кортеж
        str_ = ''.join(str_) #лепим из котрежа строку
        some_list[i+1] = str_ #и суем назад в список

print(some_list)
str_ = ' '.join(some_list)
for i in range(len(str_) - 1, 0, -1): #убираем лишние пробелы срезами
    if str_[i] == ' ' and str_[i-1].isdigit() == True:
        str_ = str_[:i] + str_[i + 1:]
        str_ = ''.join(str_)
    if str_[i] == ' ' and str_[i + 1].isdigit() == True:
        str_ = str_[:i] + str_[i + 1:]
        str_ = ''.join(str_)
    if str_[i] == ' ' and str_[i + 1] == "+":
        str_ = str_[:i] + str_[i + 1:]
        str_ = ''.join(str_)

print(str_)



