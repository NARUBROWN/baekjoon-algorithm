t = int(input())

for _ in range(t):
    stack = []
    a = input()
    for b in a:
        if b == "(":
            stack.append("(")
        if b == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")
