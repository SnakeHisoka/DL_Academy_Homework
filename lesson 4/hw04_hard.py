# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

import re
def search_nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b
def search_nok(a, b):
    return a * b / search_nod(a, b)
def diff(lst):
    difference = lst[0]
    for x in range(len(lst)):
        if x:
            difference = difference - lst[x]
    return difference
def format_dec(num, NOK):
    if num > NOK:
        cel = num // NOK
        new_num = num % NOK
        result = '{0:.0f} {1:.0f}/{2:.0f}'.format(cel, new_num, NOK)
    else:
        result = '{0:.0f}/{1:.0f}'.format(num, NOK)
    return result
print('-' * 50)
equation = input('Введите операцию в формате 5/6 + 4/7 : ')
params = re.findall(r'[-]?[0-9]+/[0-9]+|[-]?[0-9]+', equation)
funcs = re.split(r'[-]?[0-9]+/[0-9]+|[-]?[0-9]+', equation)
nums = []
noms = []
i = 0
for param in params:
    temp = param.split('/')
    nums.append(int(temp[0]))
    if len(temp) > 1:
        noms.append(int(temp[1]))
    else:
        noms.append(1)
for p in funcs:
    if p:
        func = p.strip()
        break
NOK = search_nok(noms[0], noms[1])
for n in nums:
    nums[i] = n * NOK / noms[i]
    i += 1
print('Результат - ' + equation + ':')
if func == '+':
    print(format_dec(sum(nums), NOK))
elif func == '-':
    print(format_dec(diff(nums), NOK))
else:
    print('Действие не определено')

#-----------------------------------------------------------------------------------------------------------------------------------------
# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import re
print('-' * 50)
info_person = []
info_hours = []
info =[]
workers = open('C:/HomeWork/lesson 4/Файлы/rab.txt', 'r', encoding='utf-8')
for line in workers:
    info_person.append(re.findall(r'[А-я]+[_]?[А-я]+|[0-9]+', line))
workers.close()
hours = open('C:/HomeWork/lesson 4/Файлы/hours.txt', 'r', encoding='utf-8')
for line in hours:
    info_hours.append(re.findall(r'[А-я]+\s?[А-я]+|[0-9]+', line))
hours.close()
cvit = open('C:/HomeWork/lesson 4/Файлы/otchet.txt', 'w', encoding='utf-8')
cvit.write('Имя Фамилия Заработанная плата\n')
info_person = info_person[1:]
info_hours = info_hours[1:]
for i in info_person:
    name_one_table = i[0]
    surname_one_table= i[1]
    for n in info_hours:
        name_two_table = n[0]
        surname_two_table = n[1]
        if name_one_table == name_two_table and \
            surname_one_table == surname_two_table:
            salary = int(i[2])   
            hours_norm = int(i[4])
            hours_work = int(n[2])
            work = hours_work - hours_norm
            if work > 0:
                price = salary + \
                        (2 * (salary / hours_norm) * (hours_work - hours_norm))
            else:
                price = salary + \
                        (salary / hours_norm) * (hours_work - hours_norm)
            person_data = '{0} {1} {2:.2f}\n'.format(name_one_table,
                                                  surname_one_table,
                                                  price)
            cvit.write(person_data)
            print(person_data.strip())
cvit.close()
print('Зарплатная ведомость сформирована в файле - C:/HomeWork/lesson 4/Файлы/otchet')


#-----------------------------------------------------------------------------------------------------------------------------------------
# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

import re
dikt_fruts = dict()
with open('C:/HomeWork/lesson 4/Файлы/frukt.txt',encoding='utf-8') as inp_ut:
    for fruits in inp_ut.readlines():
        file_name = 'C:/HomeWork/lesson 4/Файлы/Фрукты Результат/frukt_{}'.format(fruits[0].upper())
        dikt_fruts[file_name] = dikt_fruts.get(file_name,'')+fruits
    
for i in dikt_fruts:
    name = '{}.txt'.format(i)
    with open(name,'w') as out:
        out.write(dikt_fruts[i])
print('Формирование файлов по именам фруктов закончено!')

