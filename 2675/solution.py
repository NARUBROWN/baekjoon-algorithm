import sys
r = int(sys.stdin.readline().rstrip())
userInputs = [sys.stdin.readline().rstrip() for _ in range(r)]

for i in range(0, r):
    parts = userInputs[i].split()
    s = int(userInputs[i][0])

    for j in parts[1]:
        print(j * s, end="")
    print()

