# -*- coding: utf-8 -*-

import csv, re


with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

csv_keys = contacts_list[0]
contacts_dict = {}

def write_dict(lastname: str, firstname: str, surname: str, organization: str, position: str, phone: str, email: str) -> None:
    # ЧЕРЕЗ DICT ОБЪЕДИНЯЕМ ЗАПИСИ, ИЗБАВЛЯЕМСЯ ОТ ДУБЛЕЙ
    contact_name = '{} {}'.format(lastname, firstname)
    if contacts_dict.get(contact_name) == None:
        data = {}
        for key in csv_keys:
            data[key] = ''
    else:
        data = contacts_dict.get(contact_name)
        
    counter = 0
    values = [lastname,firstname,surname,organization,position,phone,email]
    for key in csv_keys:
        if len(data[key]) < len(values[counter]):
            data[key] = values[counter]
        counter += 1
        
    contacts_dict[contact_name] = data

def write_list() -> list:
    # ИЗВЛЕКАЕМ ДАННЫЕ ИЗ DICT В LIST
    contacts_list = []
    contacts_list.append(csv_keys)
    for contact in contacts_dict.keys():
        data = []
        for key in csv_keys:
            data.append(contacts_dict[contact][key])
        contacts_list.append(data)
    return contacts_list

def phonebook_manager(contacts_list: list) -> list:
    """
    FORMATTING PHONEBOOK DATA, DELETING DUPLICATES

    RETURN: BEAUTIFUL LIST WITH CONTACTS
    """
    pattern = r"(\+7|8)[\s\(]*(\d{3})[\)\s-]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*"

    for user_data in contacts_list[1:]:
        # ЗАБИРАЕМ ФИО С ПЕРВЫХ 3-Х ЯЧЕЕК СПИСКА
        full_name = " ".join(user_data[:3]).split(" ")

        # КОРРЕКТИРУЕМ SUBTITUTION В ЗАВИСИМОСТИ ОТ ФОРМАТА ТЕЛ.
        if "доб." in str(user_data[5]).lower():
            sub = r"+7(\2)\3-\4-\5 \6\7"
        else:
            sub = r"+7(\2)\3-\4-\5"

        write_dict(
            lastname=full_name[0],
            firstname=full_name[1],
            surname=full_name[2],
            organization=user_data[3],
            position=user_data[4],
            phone=re.sub(pattern, sub, user_data[5]),
            email=user_data[6]
            )
        
    contacts_list = write_list()
    return contacts_list

contacts_list = phonebook_manager(contacts_list)

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)