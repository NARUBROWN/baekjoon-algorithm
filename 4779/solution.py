def make(lst, now, l):
    if l == 1:
        lst[now] = '-'
    else:
        make(lst, now, l // 3)
        make(lst, now + (l * 2) // 3, l // 3)


while True:
    try:
        n = int(input())
        l = 3 ** n
        lst = [" "] * l

        make(lst, 0, l)

        print("".join(lst))
    except:
        break
