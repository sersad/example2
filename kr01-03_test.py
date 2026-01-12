"""
До пустой строки вводятся строки, в которых числа записаны через запятую и пробел (например: 123, -45, 6789).
Составьте и выведите словарь со следующими ключами (форматировать вывод словаря не нужно):

largest — самое большое число, содержащее цифры 3 или 5 (или -1, если таких чисел нет);
longest — самое длинное число по количеству цифр (игнорируя знак), не содержащее ни 3, ни 5 (первое из таких при равной длине или -1, если их нет);
counts — количество чисел, содержащих и 3, и 5 (обязательно обе цифры, порядок не важен);
average — среднее арифметическое всех чисел (округлённое до 2 знаков после запятой, или 0.0, если чисел нет);
sum_positive — сумма всех положительных чисел (или 0, если таких нет);
sum_negative — сумма всех отрицательных чисел (или 0, если таких нет).

Примечание:
При проверке наличия цифр 3 или 5 рассматривается абсолютное значение числа (без знака).
Числа могут быть отрицательными.

Например:
'450371' → содержит 3 и 5, длина = 6.
'-35' → строка '35' → содержит 3 и 5 длина = 2.

Пример 1
Ввод:
```
12, -34, 505, 9876
35, -135, 444
22, -999, 803719004, 123456789
```
Ввывод:
```
{
    'largest': 803719004,
    'longest': 9876,
    'counts': 3,
    'average': 84289592.64,
    'sum_positive': 927186687,
    'sum_negative': -1168
}
```
Пример 2
Ввод:
```
62, -8404, 203, 15768171, 679, 9344252, 1768703
345878
67335, 1700, 7704, 5541453, 8597, 450371, 71, 9238, 85629882
255, 78, 6674, 803719004, 42901, 987
```
Ввывод:
```
{

    'largest': 803719004,
    'longest': 42901,
    'counts': 5,
    'average': 40117643.22,
    'sum_positive': 922714198,
    'sum_negative': -8404
}
```
"""

# Инициализация переменных
all_numbers = []
numbers_with_3_or_5 = []
numbers_with_both_3_and_5 = []
numbers_without_3_and_5 = []

# Чтение строк до пустой строки с моржовым оператором
while (line := input()) != "":
    parts = line.split(", ")
    for part in parts:
        num = int(part)
        all_numbers.append(num)

        # Приводим к строке без знака для анализа цифр
        num_str = str(num)
        if num_str[0] == '-':
            num_str = num_str[1:]

        has_3 = '3' in num_str
        has_5 = '5' in num_str

        if has_3 or has_5:
            numbers_with_3_or_5.append(num)
        if has_3 and has_5:
            numbers_with_both_3_and_5.append(num)
        if not has_3 and not has_5:
            numbers_without_3_and_5.append(num)

# largest
if numbers_with_3_or_5:
    largest = numbers_with_3_or_5[0]
    for n in numbers_with_3_or_5:
        if n > largest:
            largest = n
else:
    largest = -1

# longest
longest = -1
max_len = -1
for n in numbers_without_3_and_5:
    num_str = str(n)
    if num_str[0] == '-':
        num_str = num_str[1:]
    current_len = len(num_str)
    if current_len > max_len:
        max_len = current_len
        longest = n

# counts
counts = len(numbers_with_both_3_and_5)

# sum_positive и sum_negative
sum_positive = 0
sum_negative = 0
for n in all_numbers:
    if n > 0:
        sum_positive += n
    elif n < 0:
        sum_negative += n

# average
if len(all_numbers) == 0:
    average = 0.0
else:
    total = 0
    for n in all_numbers:
        total += n
    average = round(total / len(all_numbers), 2)

# Вывод результата
result = {
    'largest': largest,
    'longest': longest,
    'counts': counts,
    'average': average,
    'sum_positive': sum_positive,
    'sum_negative': sum_negative
}

print(result)