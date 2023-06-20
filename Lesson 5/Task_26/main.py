"""
Задача 26: Напишите программу, которая на вход принимает два числа А и В, и возводит число А
в целую степень В с помощью рекурсии.
Пример:
А = 3; В = 5 -> 243 (3^5)
А = 2; В = 3 -> 8
"""
num_a, num_b = map(int, input(f"Введите через пробел числа А и В: ").split())

def Exp(num_a, num_b):
    try:
        i = 1
        sq = 0
        for i in range(num_b):
            sq = num_a * Exp(num_a, num_b)
        # print(sq)
        print(f"{num_a}^{num_b} -> {sq}")
    except Exception as e:
        print(f'Вы ввели не число, перезапустите программу!')

print(Exp(num_a, num_b))