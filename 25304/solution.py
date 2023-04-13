import sys

x = int(sys.stdin.readline())
repeat = int(sys.stdin.readline())

sumResult = 0

for i in range(repeat):
    a = list(map(int, sys.stdin.readline().split()))
    sumResult += a[0] * a[1]

if sumResult == x:
    print("Yes")
else:
    print("No")