# -*- coding: utf-8 -*-


def reading_files(files: list) -> dict:
    "ГЕНЕРИРУЕТ СЛОВАРЬ С КЛЮЧОМ В ВИДЕ КОЛ-ВА СТРОК"
    files_params = {}
    for file in files:
        with open(file, encoding="utf-8") as f:
            count_string = 0
            for line in f:
                count_string += 1
        if files_params.get(count_string) is None:
            files_params[count_string] = [f"{file}"]
        else:
            value = files_params[count_string]
            value.append(file)
            files_params[count_string] = value
    return files_params

def write_sorted_file(file_list: list, target_file: str) -> None:
    "ЗАПИСЫВАЕТ ДАННЫЕ В ОТДЕЛЬНЫЙ ФАЙЛ НА ОСНОВЕ СОРТИРОВАННЫХ КЛЮЧЕЙ"
    files_params = reading_files(file_list)
    sorted_list = sorted(files_params.keys())
    for key in sorted_list:
        list = files_params[key]
        for file in list:
            with open(file, encoding="utf-8") as f:
                data = (f.read()).strip()

            with open(target_file, "a", encoding="utf-8") as f:
                f.write(f"{file}\n{key}\n{data}\n")


write_sorted_file(["1.txt", "2.txt", "3.txt"], "result.txt")