import datetime
def calculate_salary():
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Module salary is imported successfully")

def salary_calculator(hours_worked, hour_rate):
    return hours_worked * hour_rate

if __name__ == '__main__':
    calculate_salary()