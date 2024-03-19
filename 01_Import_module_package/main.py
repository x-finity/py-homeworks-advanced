from application.salary import calculate_salary
from application.db.people import get_employees
import art

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    art.tprint("3a4et")