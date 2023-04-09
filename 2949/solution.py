r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
degree = int(input())


def display(degree):
    return


blank = " "

# 45
print("45\n")
# 1번째 줄에서 3번째 줄
for row in reversed(range(r)):
    # 0번째부터 2번까지 반복
    for repeat in range(1, 3):
        # 1번이면 1번 반복
        for a in range(repeat):
            print(blank * a + "A", end="")
    print()

# 4~7줄
for row in range(1, c):
    print(blank * row + "B")

print()
# 90
print("90\n")
for i in range(c):
    for j in reversed(range(r)):
        print(arr[j][i], end="")
    print()

print()
 # 0
print("0\n")
for i in range(r):
    for j in range(c):
        print(arr[i][j], end="")
    print()

print(degree)