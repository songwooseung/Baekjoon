# 3040
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
            
        
              