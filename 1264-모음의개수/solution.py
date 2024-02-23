dic = ['a', 'e', 'i', 'o', 'u']


def count(a: str):
    count = 0
    for i in a:
        if i in dic:
            count += 1
    print(count)


while True:
    n = input().lower()
    if n == "#":
        break
    count(n)
