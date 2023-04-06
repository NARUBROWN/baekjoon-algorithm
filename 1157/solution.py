word = input().upper()
unique_word = set(word)
frequency = {}

for i in unique_word:
    frequency[i] = word.count(i)

dic_list = list(frequency.values())

if dic_list.count(max(dic_list)) <= 1:
    print(max(frequency, key=frequency.get))
else:
    print("?")




