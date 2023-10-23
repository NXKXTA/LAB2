# 4
n = int(input("Введите сюда число, фактoриал котрого искать надо:"))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(f"Факториал введённого числа = {factorial}")
