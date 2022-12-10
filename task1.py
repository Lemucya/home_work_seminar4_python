"""
1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, hours_production, rate_per_hour, bonus = argv

print("Имя скрипта: ", script_name)
print("\n<< Программа расчета заработной платы сотрудника >>")
print("Выработка в часах: ", hours_production)
print("Ставка в час: ", rate_per_hour)
print("Премия: ", bonus)
print("Зарплата сотрудника: ",
      (float(hours_production) * float(rate_per_hour)) + float(bonus))

"""
вариант преподавателя

import sys
import argparse

f_obj, name_v, rate_v, hours_v = sys.argv
print(f_obj)

def calculate_salary(rate, hours):
      try:
            print(f'Сотрудник {name_v} заработал {int(rate) * int(hours) * 1.25}')
      except TypeError:
            print("Операция применена к объекту несоответствующего типа")
            exit()
            
calculate_salary(rate_v, hours_v)
"""