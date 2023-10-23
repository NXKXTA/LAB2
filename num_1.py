# 1
m = "000000000"
n = ""
lucky = 0
while len(m) > 6 or len(n) > 6:
    n = input("Введите меньший номер билета:")
    m = input("Введите больший номер билета:")

for i in range(int(n), int(m) + 1):
    ticket = "000000"
    ticket = ticket[len(str(i)) :]
    ticket = ticket + str(i)
    if int(ticket[0]) + int(ticket[1]) + int(ticket[2]) == int(ticket[3]) + int(
        ticket[4]
    ) + int(ticket[5]):
        lucky += 1

print(f"Количество счастливых билетов = {lucky}")
