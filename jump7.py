number = range(1,101)
for a in number:
    if a % 7 == 0:
        continue
    elif a % 10 == 7:
        continue
    elif a // 7 == 7:
        continue
    print(a)
