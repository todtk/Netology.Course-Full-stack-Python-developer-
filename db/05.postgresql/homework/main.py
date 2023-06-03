# -*- coding: utf-8 -*-

import psycopg2


class db_manager():
    def __init__(self, cur: psycopg2.extensions.cursor):
        cur = cur

    def create_db(self) -> None:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS clients (
            user_id SERIAL PRIMARY KEY,
            first_name VARCHAR(20) NOT NULL,
            last_name VARCHAR(20) NOT NULL,
            email VARCHAR(50) UNIQUE NOT NULL );

            CREATE TABLE IF NOT EXISTS phones (
            phone VARCHAR(14) UNIQUE NOT NULL,
            user_id SERIAL REFERENCES clients(user_id) );
            """
        )
        conn.commit()

    def add_client(self, first_name: str, last_name: str, email: str, phone: str = None) -> None:
        if self.find_client(email) == []:
            if self.find_phone(phone) == []:
                values = ({'first_name': first_name.capitalize(), 'last_name': last_name.capitalize(), 'email': email.lower()})
                cur.execute(
                    """
                    INSERT INTO clients(first_name, last_name, email)
                        VALUES(%(first_name)s, %(last_name)s, %(email)s)
                        RETURNING user_id ;
                        """, values
                )
                user_id = cur.fetchone()
                print('ADDED client ID {}'.format(user_id[0]))
                if phone is not None:
                    self.add_phone(phone, email)
            else:
                print('ERROR phone {} is busy'.format(phone))
        else:
            print('ERROR email {} is busy'.format(email))

    def update_client(self, email: str, type: str, new_value: str) -> None:
        client = self.find_client(email)
        if client != []:
            if type == 'first_name':
                values = ({'new_value': new_value.capitalize(), 'id': client[0][0]})
                cur.execute(
                    """
                    UPDATE clients AS c
                        SET first_name = %(new_value)s
                        WHERE user_id = %(id)s
                        RETURNING * ;
                    """, values
                )
                client = cur.fetchone()
            elif type == 'last_name':
                values = ({'new_value': new_value.capitalize(), 'id': client[0][0]})
                cur.execute(
                    """
                    UPDATE clients AS c
                        SET last_name = %(new_value)s
                        WHERE user_id = %(id)s
                        RETURNING * ;
                    """, values
                )
                client = cur.fetchone()
            elif type == 'email':
                if self.find_client(new_value) == []:
                    values = ({'new_value': new_value.lower(), 'id': client[0][0]})
                    cur.execute(
                        """
                        UPDATE clients AS c
                            SET email = %(new_value)s
                            WHERE user_id = %(id)s
                            RETURNING * ;
                        """, values
                    )  
                    client = cur.fetchone()
                else:
                    print('ERROR client email {} is busy'.format(email))
                    return
            print('UPDATED client ID {}'.format(client[0]))

    def delete_client(self, email: str) -> None:
        client = self.find_client(email)
        if client != []:
            values = ({'email': email.lower(), 'user_id': client[0][0]})
            cur.execute(
                """
                DELETE FROM phones AS p
                    WHERE p.user_id = %(user_id)s ;

                DELETE FROM clients AS c
                    WHERE c.email = %(email)s
                    RETURNING * ;
                """, values
            )
            client = cur.fetchone()
            print('DELETED client ID {}'.format(client[0]))
        else:
            print('ERROR client email {} not found'.format(email))

    def find_client(self, request: str) -> tuple:
        results = []
        splited_string = request.split()
        for word in splited_string:
            if '@' in word:
                values = ({'email': word.lower()})
                cur.execute(
                    """
                    SELECT *
                    FROM clients AS c
                    WHERE c.email = %(email)s
                    """, values
                )
                users_data = cur.fetchall()
                
            elif '+' == word[0]:
                phone_data = self.find_phone(word)
                try:
                    user_id = phone_data[0][1]
                    values = ({'user_id': user_id})
                    cur.execute(
                        """
                        SELECT *
                        FROM clients AS c
                        WHERE c.user_id = %(user_id)s
                        """, values
                    )
                    users_data = cur.fetchall()
                except IndexError:
                    pass
                
            else:
                values = ({'name': word.capitalize()})
                cur.execute(
                    """
                    SELECT *
                    FROM clients AS c
                    WHERE c.first_name = %(name)s OR c.last_name = %(name)s
                    """, values
                )
                users_data = cur.fetchall()

            try:
                for user in users_data:
                    if user not in results:
                        results.append(user)
            except UnboundLocalError:
                pass
        return results

    def add_phone(self, phone: str, email: str) -> None:
        if self.find_phone(phone) == []:
            if '+' in phone:
                client = self.find_client(email)
                values = ({'phone': phone, 'user_id': client[0][0]})
                cur.execute(
                    """
                    INSERT INTO phones(phone, user_id)
                        VALUES(%(phone)s, %(user_id)s)
                        RETURNING phone ;
                    """, values
                )
                phone = cur.fetchone()
                print('ADDED phone {} for client ID {}'.format(phone[0], client[0][0]))
            else:
                print('ERROR phone must start with country code +...')
        else:
            print('ERROR phone {} is busy'.format(phone))

    def delete_phone(self, phone: str) -> None:
        if self.find_phone(phone) != []:
            if '+' in phone:
                values = ({'phone': phone})
                cur.execute(
                    """
                    DELETE FROM phones AS p
                        WHERE p.phone = %(phone)s
                        RETURNING * ;
                    """, values
                )
                phone = cur.fetchone()
                print('DELETED phone {}'.format(phone[0]))
            else:
                print('ERROR phone must start with country code +...')
        else:
            print('ERROR phone {} missing'.format(phone))

    def find_phone(self, phone: str) -> tuple:
        values = ({'phone': phone})
        cur.execute(
            """
            SELECT *
            FROM phones AS p
            WHERE p.phone = %(phone)s
            """, values
        )
        phone_data = cur.fetchall()
        return phone_data


if __name__ == '__main__':
    """КОД ДЕМОНСТРИРУЮЩИЙ РАБОТУ ВСЕХ НАПИСАННЫХ ФУНКЦИЙ"""
    with psycopg2.connect(database='clients_db', user='postgres', password='[PASSWORD]') as conn:
        cur = conn.cursor()
        db = db_manager(cur)

        #СОЗДАЁМ БАЗУ ДАННЫХ
        db.create_db()

        #ДОБАВЛЯЕМ КЛИЕНТА С ТЕЛЕФОНОМ
        db.add_client('Иван', 'Иванов', 'IvanIvanon@gmail.com', '+78005553535')
        #ДОБАВЛЯЕМ КЛИЕНТА БЕЗ ТЕЛЕФОНА
        db.add_client('Пётр', 'Петров', 'PetrPetrov@mail.ru')
        #ДОБАВЛЯЕМ ОДНОФАМИЛЬЦА
        db.add_client('Василий', 'Петров', 'VasyaPetrov@bk.ru')
        print()
        
        #ДОБАВЛЯЕМ ТЕЛЕФОН
        db.add_phone('+78008008888', 'PetrPetrov@mail.ru')
        print()

        #УДАЛЯЕМ ТЕЛЕФОН
        db.delete_phone('+78008008888')
        print()
        
        #ИЩЕМ КЛИЕНТА ПО ФАМИЛИИ
        print(db.find_client('Петров'))
        #ИЩЕМ КЛИЕНТА ПО ИМЕНИ
        print(db.find_client('ИВАН'))
        #ИЩЕМ КЛИЕНТА ПО ПОЧТЕ
        print(db.find_client('PETRPETROV@MAIL.RU'))
        #ИЩЕМ КЛИЕНТА ПО ТЕЛЕФОНУ
        print(db.find_client('+78005553535'))
        print()

        #ИЗМЕНЯЕМ ДАННЫЕ КЛИЕНТА
        db.update_client('PetrPetrov@mail.ru', 'first_name', 'Игорь')
        db.update_client('PetrPetrov@mail.ru','email', 'IgorPetrov@mail.ru')
        #ПОВТОРНО ИЩЕМ КЛИЕНТА
        print(db.find_client('Петров'))
        print()

        #ДОБАВЛЯЕМ НЕСКОЛЬКО ТЕЛЕФОНОВ ЧТОБЫ ПОКАЗАТЬ КОРРЕКТНОСТЬ РАБОТЫ DELETE_CLIENT
        db.add_phone('+78000000001', 'VasyaPetrov@bk.ru')
        db.add_phone('+78000000002', 'VasyaPetrov@bk.ru')
        db.add_phone('+78000000003', 'VasyaPetrov@bk.ru')
        #УДАЛЯЕМ КЛИЕНТА
        db.delete_client('VasyaPetrov@bk.ru')
        #ПОВТОРНО ИЩЕМ КЛИЕНТА
        print(db.find_client('VasyaPetrov@bk.ru'))

    conn.close()