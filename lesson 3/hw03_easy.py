# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
for index, value in enumerate(fruits):
    print('{} {:>6}'.format(str(index + 1) + '.', value))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

b = {'h', 'r', 'j', 'q', 'k', 'l'}
d = {'l', 'h', 'j', 'q'}
c = b - d
print(list(c))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

ls3 = [2, 7, 5, 6, 9, 15]
new_list = [i / 4 if i % 2 == 0 else i * 2 for i in ls3]
print(new_list)