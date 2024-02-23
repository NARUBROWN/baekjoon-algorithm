hour, minute, second = map(int, input().split())
second = second + int(input())
minute = minute + second//60
hour = hour + minute//60


print(hour, minute, second)