# -*- coding: utf-8 -*-

import sqlalchemy, os
from time import sleep
from sqlalchemy.orm import sessionmaker

from models import Book, Publisher, Sale, Shop, Stock, create_tables

username = 'postgres'
password = ''
db_name = 'book_db'

DSN = f'postgresql://{username}:{password}@localhost:5432/{db_name}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

#ЗАПОЛНЯЕМ ДАННЫЕ
publisher_1 = Publisher(id=1, name='Swaroop Chitlur')
publisher_2 = Publisher(id=2, name='Aditya Bhargava')
book_1 = Book(id=1, title='A Byte of Python', id_publisher=publisher_1.id)
book_2 = Book(id=2, title='Grokking Algorithms', id_publisher=publisher_2.id)
shop_1 = Shop(id=1, name='ЛитРес')
stock_1 = Stock(id=1, id_book=book_1.id, id_shop=shop_1.id, count=12320)
stock_2 = Stock(id=2, id_book=book_2.id, id_shop=shop_1.id, count=19006)
session.add_all([publisher_1, publisher_2, book_1, book_2, shop_1, stock_1, stock_2])
session.commit()

def publisher_search():
    os.system("cls")
    while True:
        response = input('Введите ID или Имя автора: ')
        if response.isdigit() is True:
            for query in session.query(Publisher).filter(Publisher.id == int(response)).all():
                print(query)
        else:
            for query in session.query(Publisher).filter(Publisher.name.like(response)).all():
                print(query)
        sleep(2)
        os.system("cls")

publisher_search()
session.close()