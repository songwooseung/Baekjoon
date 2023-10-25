# 3040
# 방법 1 
dwerfs = []
x = 0
y = 0
num = 0
for i in range(9):
    dwerfs.append(int(input()))
    num += dwerfs[i]
num -= 100

for i in range(8):
    for j in range(i+1,9):
        if dwerfs[i] + dwerfs[j] == num :
            x = dwerfs[i]
            y = dwerfs[j]
            break

for i in range(9):
    if dwerfs[i] == x or dwerfs[i] == y:
        continue
    else :
        print(dwerfs[i])
'''
# 방법 2 sum() 함수 사용
dwarf = []
x = 0
y = 0
for i in range(9):
    dwarf.append(int(input()))
for i in range(8):
    for j in range(i+1, 9):
        if sum(dwarf)-dwarf[i]-dwarf[j] == 100:
            x = i
            y = j
for i in range(9):
    if i != x and i != y:
        print(dwarf[i])
''' 