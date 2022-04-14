from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

edit_list = []
sum_list = []
complite_list = []

# Функция производит провеку входящей записи по всем элементам исходного листа,
# находя пустое значение заполняет из совпадающего по условию (проверка фамелии и имени)
def fusion(check_list, fusion_list):
    for entry in range(len(fusion_list)):
        if check_list[0] == fusion_list[entry][0] and check_list[1] == fusion_list[entry][1]:
            for element in range(len(fusion_list[0])):
                if check_list[element] == '':
                    check_list[element] = fusion_list[entry][element]
    return check_list


with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
# Поступающие данные "грязные" в разных записях разное количество полей, обрезаем до длинны заголовка файла
# Разбивка полей адресной книги по словам и заполнение ИФО по полям
# Формируем список по ФИО (первые 3 элемента), преобразуем в строку и разбиваем по словам
# Функция findall выдает на выходе список
limit = len(contacts_list[0])
for entry in range(len(contacts_list)):
    if len(contacts_list[entry]) > limit:
        del (contacts_list[entry])[limit:]
    for element in range(3):
        edit_list.append(contacts_list[entry][element])
    book_names = (' '.join(edit_list))
    pattern = r'\w+'
    edit_list = re.findall(pattern, book_names)

# Объединяем списки по каждой записи, удаляя первые элементы исходного списка
    for index in range(len(edit_list)):
        contacts_list[entry].pop(0)
    contacts_list[entry] = edit_list + contacts_list[entry]
    edit_list.clear()

# Форматируем телефоны в соответсвующем поле (элементе списка)
work_pattern = r'(\+7|8)?[\s(]*(\d{3})[\s)]*[\s-]*(\d{3})*[\s-]*(\d{2})[\s-]*(\d{2})?[\s(]*(\доб\.)*[\s]*(\d+)?[\)]?'
format_pattern = r'+7(\2)\3-\4-\5 \6\7'
for entry in range(len(contacts_list)):
    contacts_list[entry][5] = re.sub(work_pattern, format_pattern, contacts_list[entry][5])

# Объединяем данные каждой записи списка с совпадающими
for index in range(len(contacts_list)):
    fusion(contacts_list[index], contacts_list)
# Переносим несовпадающие записи в новый список
for item in contacts_list:
    if item not in complite_list:
        complite_list.append(item)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(complite_list)
