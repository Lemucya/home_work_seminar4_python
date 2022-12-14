"""
2) Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для
формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

result_list = []
list_user = [int(i) for i in input("Введите список чисел: ").split()]
for i in range(1, len(list_user)):
    if list_user[i] > list_user[i - 1]:
        (result_list.append(list_user[i]))
print("Исходный список: ", list_user)
print("Список, элементы которого больше предыдущего: ", result_list)

"""
вариант преподавателя:

primary_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# вариант без генераторного выражения
res_list_1 = []
for ei in range(1, len(primary_list)):
    if primary_list[el] > primary_list[el - 1]:
        res_list_1.append(primary_list[el])
        
print(res_list_1)

# вариант с генераторным выражением c LC
res_list_2 = [primary_list[el] for el in range(
    1, len(primary_list)) if primary_list[el] > primary_list[el - 1]]
    
print(res_list_2)
"""