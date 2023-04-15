import sys

n, k = map(int, sys.stdin.readline().split())

by_name = {}
by_number = {}

for i in range(n):
    name = sys.stdin.readline().rstrip()
    by_name[name] = i
    by_number[i] = name

for j in range(k):
    x = sys.stdin.readline().rstrip()
    if x.isalpha():
        print(int(by_name[x]) + 1)
    else:
        print(by_number[int(x) - 1])