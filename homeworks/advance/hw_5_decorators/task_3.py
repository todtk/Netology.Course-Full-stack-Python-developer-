# -*- coding: utf-8 -*-

import csv, re
from datetime import datetime


def logger(path: str = "logger.log"):
    
    def __logger(old_function):

        datetime_ = datetime.strftime(datetime.now(), r'%d/%m/%y %H:%M:%S')

        def new_function(*args, **kwargs):

            result = old_function(*args, **kwargs)
            text = f"{datetime_}, func: {old_function.__name__}, args: {args, kwargs}, result: {result}\n"

            with open(path, "a") as file:
                file.write(text)

            return result

        return new_function

    return __logger

# CODE FROM REGEX HOMEWORK
# ORIGINAL REPO https://github.com/todtk/Netology.Course_Full.Stack.Python.Developer/tree/main/homeworks/advance/hw_2_regexp
with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

csv_keys = contacts_list[0]
contacts_dict = {}

@logger()
def write_dict(
        lastname: str,
        firstname: str,
        surname: str,
        organization: str,
        position: str,
        phone: str,
        email: str) -> None:

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

@logger()
def write_list() -> list:
    contacts_list = []
    contacts_list.append(csv_keys)
    for contact in contacts_dict.keys():
        data = []
        for key in csv_keys:
            data.append(contacts_dict[contact][key])
        contacts_list.append(data)
    return contacts_list

@logger()
def phonebook_manager(contacts_list: list) -> list:
    """
    FORMATTING PHONEBOOK DATA, DELETING DUPLICATES

    RETURN: BEAUTIFUL LIST WITH CONTACTS
    """
    pattern = r"(\+7|8)[\s\(]*(\d{3})[\)\s-]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*"

    for user_data in contacts_list[1:]:
        full_name = " ".join(user_data[:3]).split(" ")

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