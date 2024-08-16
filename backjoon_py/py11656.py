word = input()
res = []

for i in range(len(word)):
    res.append(word[i:])

for i in sorted(res):
    print(i)