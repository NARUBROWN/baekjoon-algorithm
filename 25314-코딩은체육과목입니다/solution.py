import sys
input = sys.stdin.readline().rstrip()

n = int(input) / 4
for i in range(0, int(n)):
    print("long", end=" ")

print("int")