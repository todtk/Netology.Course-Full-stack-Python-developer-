# -*- coding: utf-8 -*-

from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    print(datetime.date(datetime.now()), calculate_salary())
    print(datetime.date(datetime.now()), get_employees())