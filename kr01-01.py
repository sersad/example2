"""
Напишите программу для выбора строк, содержащих магию, другими словами, удовлетворяющих условиям:

все слова в строке начинаются с прописной буквы, а остальные — строчные;
заканчивается строка на точку или точку с запятой;
длина строки кратна трём или пяти.
Вводится количество строк, затем сами строки.
Выведите выбранные строки в исходном порядке.

Пример 1
Ввод
5
It Was A Little Depressing
For The Girl.
Somehow Everything Turned Out;
To Be Too Decent;
Just Be Good and Help Everyone.

Вывод
Somehow Everything Turned Out;

Пример 2
Ввод
6
Anyway,
What Witches Do Is Like A Job.
Boring Job.
And Tiffany Was
Depressingly Good;
At Not Using Magic.

Вывод
What Witches Do Is Like A Job.
Depressingly Good;
"""

for _ in range(int(input())):
    s = input()
    if all(i.istitle() for i in s.split()) and s[-1] in '.;' and (len(s) % 3 == 0 or len(s) % 5 == 0):
        print(s)
