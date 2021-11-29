
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 3, 4, 1, 2, 6 ,7 ,8]
c = 0
for i in range(7):
    x1 = x[i]
    y1 = y[i]
    for j in range(i+1, 8):
        x2 = x[j]
        y2 = y[j]
        if x1 == x2 or y1 == y2 or (abs(x1 - x2) == abs(y1 - y2)):
            print('YES')
            exit()
print('NO')