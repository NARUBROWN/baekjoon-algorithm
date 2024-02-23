from sys import stdin

dic = {}


def binary_search(element, arr):
    count = 0
    start_point = 0
    end_point = len(arr) - 1
    while start_point <= end_point:
        mid_point = (start_point + end_point) // 2
        if element == arr[mid_point]:
            count += 1
        if element > arr[mid_point]:
            start_point = mid_point + 1
        else:
            end_point = mid_point - 1
    return count


N = int(stdin.readline())
card_number = sorted(map(int, stdin.readline().split()))
M = int(stdin.readline())
user_number = map(int, stdin.readline().split())
