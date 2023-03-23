# -*- coding: utf-8 -*-


"""ОБЪЯВЛЯЮ БАЗОВЫЕ ПЕРЕМЕННЫЕ"""
interest_rate = 15.0
amount_children = 0

"""ПОЛУЧАЮ ДАННЫЕ ПОЛЬЗОВАТЕЛЯ"""
region = input("Укажите регион.\n")

have_children = input("Есть дети?\n")

if have_children.lower() == "да":
  
  amount_children = int(input("Укажите кол-во детей.\n"))
  
partner_program = input("Являетесь зарплатным клиентом нашего банка?\n")

insurance = input("Будете ли оформлять страхование в нашем банке?\n")

"""СЧИТАЮ И ВЫВОЖУ СТАВКУ"""
if region.lower() == "дальний восток":
  
  interest_rate = 2.0
  print(f"Вы можете получить ипотечный кредит в нашем банке по ставке {interest_rate}%.\n\n")
  
elif region.lower() in ["поволжье", "урал", "сибирь"]:

  if amount_children > 3:
    
    interest_rate = interest_rate - 1

  if partner_program == "да":
    
    interest_rate = interest_rate - 0.5

  if insurance == "да":

    interest_rate = interest_rate - 1.5
    
  print(f"Вы можете получить ипотечный кредит в нашем банке по ставке {interest_rate}%.\n\n")