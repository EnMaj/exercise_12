month = 1

year = 2001
summ = 0
day_sec = 24*60*60

for i in range(1, month):
    if i in [4, 6, 9, 11]:
        summ += 30 * day_sec
    else:
        summ += 31 * day_sec

print(summ)