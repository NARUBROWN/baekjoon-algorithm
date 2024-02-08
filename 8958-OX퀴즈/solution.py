import sys

repeat = int(sys.stdin.readline().rstrip())

inputs = [sys.stdin.readline().rstrip() for _ in range(repeat)]


for i in range(0, len(inputs)):
    point = 0
    continuous = 0
    for j in range(0, len(inputs[i])):
        if inputs[i][j] == 'O':
            continuous += 1
            point = point + continuous
        else:
            continuous = 0
    print(point)

