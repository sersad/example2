s = ["12, -34, 505, 9876",
     "35, -135, 444",
     "22, -999, 803719004, 123456789"]

largest = []
longest = []
counts = 0
summ = []
sum_positive = 0
sum_negative = 0


for line in s:
     for i in line.split(", "):
          summ.append(int(i))
          if int(i) > 0:
               sum_positive += int(i)
          else:
               sum_negative += int(i)

          if '3' in i and '5' in i:
               counts += 1
          largest.append(int(i))

          if '3' not in i and '5' not in i:
               longest.append(i)



d = {"sum_positive": sum_positive,
     "sum_negative": sum_negative,
     "counts": counts,
     "largest": max(largest),
     "longest": max(longest, key=len),
     "avarage": round(sum(summ) / len(summ), 2)
     }

print(d)