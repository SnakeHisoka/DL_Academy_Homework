# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import re
print('-' * 50)
print('Задача 2')
info_person = []
info_hours = []
info =[]
workers = open('C:/Users/tltuser127/Desktop/HomeWork/lesson 4/Файлы/workers.txt', 'r', encoding='utf-8')
for line in workers:
    info_person.append(re.findall(r'[А-я]+[_]?[А-я]+|[0-9]+', line))
workers.close()
hours = open('C:/Users/tltuser127/Desktop/HomeWork/lesson 4/Файлы/hours_of.txt', 'r', encoding='utf-8')
for line in hours:
    info_hours.append(re.findall(r'[А-я]+\s?[А-я]+|[0-9]+', line))
hours.close()
cvit = open('C:/Users/tltuser127/Desktop/HomeWork/lesson 4/Файлы/vedomost.txt', 'w', encoding='utf-8')
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
            salary = int(i[2])      # оклад
            hours_norm = int(i[4])  # норма отработанных часов
            hours_work = int(n[2])  # отработано часов
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
print('Зарплатная ведомость сформирована в файле - C:/Users/tltuser127/Desktop/HomeWork/lesson 4/Файлы/vedomost.txt')