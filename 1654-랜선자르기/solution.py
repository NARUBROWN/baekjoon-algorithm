import sys

K, N = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
start_point = 1
end_point = max(lan)

while start_point <= end_point:
    mid_point = (start_point + end_point) // 2
    LAN = 0
    for i in lan:
        LAN += i // mid_point
    if LAN >= N:
        start_point = mid_point + 1
    else:
        end_point = mid_point - 1

print(end_point)