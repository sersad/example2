import datetime as dt  # Лень писать целиком.

s = "27/11/25"
wrong = [2, 5, 6]
x = dt.datetime.strptime(s, "%d/%m/%y")
d = dt.timedelta(days=1)
count = 0

while count < 5:
    if x.weekday() + 2 in wrong:
        x += 4 * d
    elif x.weekday() + 1 in wrong:
        x += 3 * d
    else:
        x += 2 * d
    while x.weekday() in wrong:
        x += d
    print(x, x.weekday())
    count += 1
