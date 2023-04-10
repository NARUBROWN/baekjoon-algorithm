import sys
# input 함수보다 빠름
n = int(sys.stdin.readline())

stack = []

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) != 0:
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            # 파이썬 리스트에서 -1하면 요소 맨 뒤에서 부터 접근가능
            print(stack[-1])
