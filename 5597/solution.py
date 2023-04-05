attendance = ["None"] * 30
for i in range(28):
    numbers = int(input()) - 1
    attendance[numbers] = "true"

for i in range(len(attendance)):
    if attendance[i] == 'None':
        print(i+1)





