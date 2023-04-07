n, m = map(int, input().split())
numbers = list(map(int,input().split()))
sumVar = []
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if numbers[i] + numbers[j] + numbers[k] <= m:
                sumVar.append(numbers[i] + numbers[j] + numbers[k])

print(max(sumVar))
