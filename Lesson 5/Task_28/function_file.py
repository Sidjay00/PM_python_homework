def sum(a,b,count=0):
        if a == 0:
            return b
        else:
            return 2 + sum(a-1, b-1)

a, b = map(int, input(f"Введите через пробел числа А и В: ").split())
print(sum(a,b))