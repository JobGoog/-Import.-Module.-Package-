from application.salary import calculate_salary
from application.db.people import get_employees
from application.data.datatime import time_now


if __name__ == '__main__':
    calculate_salary()
    time_now()
    get_employees()