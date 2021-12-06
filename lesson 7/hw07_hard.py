# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


class Worker:
    def __init__(self, name, surname, salary, work, normhours):
        self.name = name
        self.surname = surname
        self.salary = int(salary)
        self.work = work
        self.normhours = int(normhours)
        self.worked_hours = 0

    def salary_to_get(self):
        if self.normhours > self.worked_hours:
            salary = self.salary / self.normhours * self.worked_hours
        else:
            salary = self.salary + (self.worked_hours - self.normhours) * (self.salary / self.normhours) * 2

        print(f'{self.name} {self.surname} отработал {self.worked_hours} часов из {self.normhours} '
              f'и при окладе в {self.salary} заработал за месяц - {round(salary, 2)}')

workers = open('workers.txt')
hours = open('hours_of.txt')

workers_dict = {}

skip_1st_line = True
for line in workers:
    if skip_1st_line:
        skip_1st_line = False
    else:
        param = list(filter(lambda x: x != '', line.rstrip('\n').split(' ')))
        workers_dict[f"{param[0]} {param[1]}"] = Worker(param[0], param[1], param[2], param[3], param[4])

skip_1st_line = True
for line in hours:
    if skip_1st_line:
        skip_1st_line = False
    else:
        param = list(filter(lambda x: x != '', line.rstrip('\n').split(' ')))
        for key in workers_dict.keys():
            if key == f'{param[0]} {param[1]}':
                worker = workers_dict.get(key)
                worker.worked_hours = int(param[2])

workers.close()
hours.close()

for key in workers_dict.keys():
    workers_dict.get(key).salary_to_get()