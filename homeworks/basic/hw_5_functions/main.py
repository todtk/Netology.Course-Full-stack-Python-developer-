# -*- coding: utf-8 -*-


documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

#BASIC
def find_doc_in_docs(number):
    result = "Документ не найден"
    for document in documents:
        if document["number"] == number:
            result = document
            break
    return result

def add_doc_in_docs(number, type, name):
    result = find_doc_in_docs(number)
    if result == "Документ не найден":
        documents.append({"type": type, "number": number, "name": name})
    else:
        result = "Документ найден"
    return result

def remove_doc_from_docs(number):
    result = find_doc_in_docs(number)
    if result != "Документ не найден":
        documents.remove(result)
    else:
        return result

def show_docs_in_docs():
    for document in documents:
        print(f'''{document['type']} "{document['number']}" "{document['name']}" ''')

def find_doc_in_shelf(number):
    result = "Документ не найден"
    for key, value in directories.items():
        if number in value:
            result = [key, value]
            break
    return result    

def add_doc_in_shelf(number, shelf):
    result = find_doc_in_shelf(number)
    if result == "Документ не найден":
        if shelf in directories.keys():
            value = directories[shelf]
            value.append(number)
            directories[shelf] = value
    else:
        result = "Документ найден"
    return result

def remove_doc_from_shelf(number):
    result = find_doc_in_shelf(number)
    if result != "Документ не найден":
        value = directories[result[0]]
        value.remove(number)
        directories[result[0]] = value
    else:
        return result

#ADVANCED
def search_name():
    number = input("Введите номер документа: ")

    result = find_doc_in_docs(number)
    if result != "Документ не найден":
        result = result["name"]
    return result

def search_shelf():
    number = input("Введите номер документа: ")

    result = find_doc_in_shelf(number)
    if result != "Документ не найден":
        result = result[0]
    return result

def add_doc():
    number = input("Введите номер документа: ")
    type = input("Введите тип документа: ")
    name = input("Введите Имя и Фамилию: ")
    shelf = input("Введите номер ячейки для размещения: ")

    result = "Документ добавлен."
    if shelf in directories.keys():
        task_01 = add_doc_in_docs(number, type, name)
        task_02 = add_doc_in_shelf(number, shelf) 
        if task_01 and task_02 == "Документ найден":
            result = "Операция не выполнена. Документ уже существует"
    else:
        result = f"Операция не выполнена. Ячейка {shelf} не существует, воспользуйтесь командой 'as'."
    return result

def del_doc():
    number = input("Введите номер документа: ")

    result = "Документ удалён."
    task_01 = remove_doc_from_docs(number)
    task_02 = remove_doc_from_shelf(number)
    if task_01 and task_02 == "Документ не найден":
        result = "Документ не найден"
    return result

def move_doc():
    number = input("Введите номер документа: ")
    shelf = input("Введите номер ячейки: ")

    result = "Документ перемещён."
    if shelf in directories.keys():
        task_01 = remove_doc_from_shelf(number)
        if task_01 == "Документ не найден":
            result = "Документ не найден"
        else:
            task_02 = add_doc_in_shelf(number, shelf)
    else:
        result = f"Операция не выполнена. Ячейка {shelf} не существует, воспользуйтесь командой 'as'."
    return result

def add_shelf():
    shelf = input("Введите номер новой ячейки: ")

    result = "Ячейка добавлена."
    if shelf not in directories.keys():
        directories[shelf] = []
    else:
        result = f"Операция не выполнена. Ячейка {shelf} уже существует." 
    return result

def input_func():
    print(f"СПИСОК ОПЕРАЦИЙ\n{'-'*30}\np-искать человека\ns-искать ячейку хранения\nl-список всех документов\na-добавить документ\nd-удалить документ\nm-переместить документ\nas-добавить ячейку хранения\n{'-'*30}")
    while True:
        command = input("Выберите операцию: ")
        if command == "p":
            result = search_name()

        elif command == "s":
            result = search_shelf()

        elif command == "l":
            show_docs_in_docs()
            continue

        elif command == "a":
            result = add_doc()

        elif command == "d":
            result = del_doc()

        elif command == "m":
            result = move_doc()

        elif command == "as":
            result = add_shelf()

        elif command == "exit":
            break

        else:
            result = "Несуществующая команда"
        print(result)


input_func()