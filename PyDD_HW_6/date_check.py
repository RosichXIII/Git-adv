# 1. Решить задачи, которые не успели решить на семинаре.

# 2. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import sys

def _leap_year(year: int):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True

def date_check(date: str):
    day, month, year = list(map(int, date.split(".")))
    
    if year in range(1, 10000) and month in range(1, 13) and day in range (1, 32):
        if month in [1, 3, 5, 7, 8, 10, 12] and day in range(1, 32):
            return True
        elif month in [4, 6, 9, 11] and day in range(1, 31):
            return True
        else:
            if _leap_year(year) == True:
                if day in range(1, 30):
                    return True
            else:
                if day in range(1, 29):
                    return True
                
if __name__ == "__date_check__":
    print(date_check(sys.argv[1]))


print(date_check(input("Введите дату в формате DD.MM.YYYY: ")))