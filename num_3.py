# 3
s = int(input("Введите сумму цифр от 1 до 27 включительно:"))
if 1 <= s <= 27:
    for i in range(100, 1000):
        if sum(int(j) for j in str(i)) == s:
            print(i)
else:
    print("Введена неверная сумма цифр")
