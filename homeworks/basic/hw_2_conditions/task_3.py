# -*- coding: utf-8 -*-


"""ПОЛУЧАЮ ДАТУ РОЖДЕНИЯ ОДНИМ ВВОДОМ"""
birthday_date = input("Введите дату рождения в формате ДД.ММ.ГГ\n")
day = int(birthday_date[:2])
mounth = int(birthday_date[3:5])
year = int(birthday_date[6:])

if mounth == 1:
  
  if day in range(1, 20):
    print("Козерог")
  elif day in range(21, 31):
    print("Водолей")
  else:
    print("Неверная дата.")

elif mounth == 2:
  
  if day in range(1, 19):
    print("Водолей")
  elif day in range(20, 28):
    print("Рыбы")
  else:
    print("Неверная дата.")
  
elif mounth == 3:
  
  if day in range(1, 20):
    print("Рыбы")
  elif day in range(21, 31):
    print("Овен")
  else:
    print("Неверная дата.")
  
elif mounth == 4:
  
  if day in range(1, 20):
    print("Овен")
  elif day in range(21, 30):
    print("Телец")
  else:
    print("Неверная дата.")
  
elif mounth == 5:
  
  if day in range(1, 21):
    print("Телец")
  elif day in range(22, 31):
    print("Близнецы")
  else:
    print("Неверная дата.")
  
elif mounth == 6:
  
  if day in range(1, 21):
    print("Близнецы")
  elif day in range(22, 30):
    print("Рак")
  else:
    print("Неверная дата.")
  
elif mounth == 7:
  
  if day in range(1, 22):
    print("Рак")
  elif day in range(23, 31):
    print("Лев")
  else:
    print("Неверная дата.")
  
elif mounth == 8:
  
  if day in range(1, 21):
    print("Лев")
  elif day in range(22, 31):
    print("Дева")
  else:
    print("Неверная дата.")
  
elif mounth == 9:
  
  if day in range(1, 23):
    print("Дева")
  elif day in range(24, 30):
    print("Весы")
  else:
    print("Неверная дата.")
  
elif mounth == 10:
  
  if day in range(1, 23):
    print("Весы")
  elif day in range(24, 31):
    print("Скорпион")
  else:
    print("Неверная дата.")
  
elif mounth == 11:
  
  if day in range(1, 22):
    print("Скорпион")
  elif day in range(23, 30):
    print("Стрелец")
  else:
    print("Неверная дата.")
  
elif mounth == 12:
  
  if day in range(1, 22):
    print("Стрелец")
  elif day in range(23, 31):
    print("Козерог")
  else:
    print("Неверная дата.")

    