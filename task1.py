# Вычислить число c заданной точностью d
from cmath import pi
d = int(input("Введите число:"))
print(f'число Пи с заданной точностью {d} = {round(pi, d)}')