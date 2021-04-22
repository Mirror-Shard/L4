import math

k = int(input("Введите целое число: "))
math.sqrt(k)

for i in range(2, k):
    if k % i == 0:
        str = "не простое"
        break
    else:
        str = "простое"

print(str)