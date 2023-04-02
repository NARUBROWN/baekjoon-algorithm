number = int(input())
layer = 1
count = 1

while number > layer:
    layer += 6 * count
    count += 1

print(count)

