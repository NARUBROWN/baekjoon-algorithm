import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))
a.sort()


def binary_search(list, x):
    start = 0
    end = len(list) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == list[mid]:
            return 1
        elif x > list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0


for i in k:
    print(binary_search(a, i))
