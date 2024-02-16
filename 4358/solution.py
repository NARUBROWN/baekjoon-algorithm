import sys

dic = dict()
total = 0

while True:
    word = sys.stdin.readline().rstrip()
    if word == "":
        break
    total += 1
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

sorted_dict = dict(sorted(dic.items()))
for i in sorted_dict:
    per = sorted_dict[i] / total * 100
    print(f'{i} {per:.4f}')

