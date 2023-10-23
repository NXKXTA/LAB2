# 2
n = abs(int(input("Введите целое число n:")))
m = abs(int(input("Введите целое число m:")))

n1 = len(str(n))
m1 = len(str(m))
if n1 > m1:
    print(f"Наибольшее кол-во цифр у числа:{n}")
elif n1 < m1:
    print(f"Наибольшее кол-во цифр у числа:{m}")
else:
    print(f"Кол-во цифр чисел {n} и {m} одинаковое")
