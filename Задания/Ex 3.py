# Вариант 18
import math

k = int(input("Введите целое число: "))
math.sqrt(k)

str = "простое"

for i in range(2, k):
    if k % i == 0:
        str = "не простое"
        break

print(str)