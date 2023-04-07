n = int(input())
m = []

for i in range(n):
    a = int(input())
    m.append(a)

for i in range(n):
    for a in range(n):
        temp = m[i]
        if m[i] < m[a]:
            m[i] = m[a]
            m[a] = temp

for i in range(n):
    print(m[i])

