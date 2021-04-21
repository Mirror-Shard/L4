import math

k = (input("Введите целое число: "))
b = math.pow(k, 1/2)
i = 2

for i in range(i, k):
    if k % i == 0:
        str = "простое"
        continue
    else:
        str = "не простое"
        break

print(f"Число k - {str}")