attendance = ["None"] * 30
# 이것 보단 더 좋은 방법이 있을 듯...
for i in range(28):
    numbers = int(input()) - 1
    attendance[numbers] = "true"

for i in range(len(attendance)):
    if attendance[i] == 'None':
        print(i+1)





