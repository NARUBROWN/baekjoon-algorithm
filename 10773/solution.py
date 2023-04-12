k = int(input())
stack = []
sum = 0
for i in range(k):
    number = int(input())
    if number == 0:
        stack.pop()
    else:
        stack.append(number)

for i in range(len(stack)):
    sum += stack[i]

print(sum)