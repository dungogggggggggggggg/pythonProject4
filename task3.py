# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
lst = list(map(int, input("Введите числа:\n").split()))
print(f"Исходный список: {lst}")
New_list = []
[New_list.append(i) for i in lst if i not in New_list]
print(f'Новый список {New_list}')
