import numpy as np
import random
N = 4
J = 1

#lab3
#функция для подсчета энергии одного спина
def E_spin(arr, x, y):
    E = 0

    #1 условие центральный элемент
    if x > 0 and x < N - 1 and y > 0 and y < N - 1:
        E = -J * arr[y][x] * (arr[y][x - 1] + arr[y][x + 1] + arr[y - 1][x] + arr[y + 1][x])

    #2 условие верхний левый
    elif x == 0 and y == 0:
        E = -J * arr[y][x] * (arr[y][N - 1] + arr[y][x + 1] + arr[N - 1][x] + arr[y + 1][x])

    #3 условие верхняя грань
    elif x > 0 and x < N - 1 and y == 0:
        E = -J * arr[y][x] * (arr[y][x - 1] + arr[y][x + 1] + arr[N - 1][x] + arr[y + 1][x])

    #4 условие правый нижний
    elif x == N - 1 and y == N - 1:
        E = -J * arr[y][x] * (arr[y][x - 1] + arr[y][0] + arr[y - 1][x] + arr[0][x])

    #5 условие нижняя грань
    elif x > 0 and x < N - 1 and y == N-1:
        E = -J * arr[y][x] * (arr[y][x - 1] + arr[y][x + 1] + arr[y - 1][x] + arr[0][x])
    #6 условие левая грань
    elif x == 0 and y > 0 and y < N - 1:
        E = -J * arr[y][x] * (arr[y][N - 1] + arr[y][x + 1] + arr[y - 1][x] + arr[y + 1][x])
    #7 условие правая грань
    elif x == N - 1 and y > 0 and y < N - 1:
        E = -J * arr[y][x] * (arr[y][x - 1] + arr[y][0] + arr[y - 1][x] + arr[y + 1][x])
    #8 условие нижний левый
    elif x == 0 and y == N-1:
        E = -J * arr[y][x] * (arr[y][N - 1] + arr[y][x + 1] + arr[y - 1][x] + arr[0][x])
    #9 условие верхний правый
    elif x == N - 1 and y == 0:
        E = -J * arr[y][x] * (arr[y][x - 1] + arr[y][0] + arr[N - 1][x] + arr[y+1][x])

    return E

#функция для подсчета энергии всей системы
def E_system(arr):
    E_sys = 0
    for y in range(N):
        for x in range(N):
            E_sys += E_spin(arr, x, y)

    E_sys /= 2

    return E_sys

#arr = [[1 for x in range(N)] for y in range(N)]
arr = np.random.choice([-1, 1], (4, 4))
#arr = np.ones((N, N))
print(arr)
print("E_system =", E_system(arr))
x = random.randint(0, 3)
y = random.randint(0, 3)
print(x, '(координата x)', y, '(координата y)')
print(arr[y, x], 'Спин')


print("E_spin =", E_spin(arr, x, y))
#1 условие центральный элемент
if x > 0 and x < N - 1 and y > 0 and y < N - 1:
    print(arr[y][x - 1], 'сосед слева')
    print(arr[y][x + 1], 'сосед справа')
    print(arr[y - 1][x], 'сосед сверху')
    print(arr[y + 1][x], 'сосед снизу')
#2 условие верхний левый
elif x == 0 and y == 0:
    print(arr[y][N - 1], 'сосед слева')
    print(arr[y][x + 1], 'сосед справа')
    print(arr[N - 1][x], 'сосед сверху')
    print(arr[y + 1][x], 'сосед снизу')
    #3 условие верхняя грань
elif x > 0 and x < N - 1 and y == 0:
    print(arr[y][x - 1], 'сосед слева')
    print(arr[y][x + 1], 'сосед справа')
    print(arr[N - 1][x], 'сосед сверху')
    print(arr[y + 1][x], 'сосед снизу')
    #4 условие правый нижний
elif x == N - 1 and y == N - 1:
    print(arr[y][x - 1], 'сосед слева')
    print(arr[y][0], 'сосед справа')
    print(arr[y - 1][x], 'сосед сверху')
    print(arr[0][x], 'сосед снизу')
    #5 условие нижняя грань
elif x > 0 and x < N - 1 and y == N-1:
    print(arr[y][x - 1], 'сосед слева')
    print(arr[y][x + 1], 'сосед справа')
    print(arr[y - 1][x], 'сосед сверху')
    print(arr[0][x], 'сосед снизу')
    #6 условие левая грань
elif x == 0 and y > 0 and y < N - 1:
    print(arr[y][N - 1], 'сосед слева')
    print(arr[y][x + 1], 'сосед справа')
    print(arr[y - 1][x], 'сосед сверху')
    print(arr[y + 1][x], 'сосед снизу')
    #7 условие правая грань
elif x == N - 1 and y > 0 and y < N - 1:
    print(arr[y][x - 1], 'сосед слева')
    print(arr[y][0], 'сосед справа')
    print(arr[y - 1][x], 'сосед сверху')
    print(arr[y + 1][x], 'сосед снизу')
    #8 условие нижний левый
elif x == 0 and y == N-1:
    print(arr[y][N - 1], 'сосед слева')
    print(arr[y][x + 1], 'сосед справа')
    print(arr[y - 1][x], 'сосед сверху')
    print(arr[0][x], 'сосед снизу')
    #9 условие верхний правый
elif x == N - 1 and y == 0:
    print(arr[y][x - 1], 'сосед слева')
    print(arr[y][0], 'сосед справа')
    print(arr[N - 1][x], 'сосед сверху')
    print(arr[y+1][x], 'сосед снизу')