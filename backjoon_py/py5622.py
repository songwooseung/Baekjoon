# 5622
# 2023-10-07 07:45:45
cnt = 0
a = list(input())
for i in range(len(a)) :
    if a[i] == 'A' or a[i] =='B' or a[i] =='C' :
        cnt += 3
    elif a[i] == 'D' or a[i] =='E' or a[i] =='F' :
        cnt += 4
    elif a[i] == 'G' or a[i] =='H' or a[i] =='I' :
        cnt += 5
    elif a[i] == 'J' or a[i] =='K' or a[i] =='L' :
        cnt += 6
    elif a[i] == 'M' or a[i] =='N' or a[i] =='O' :
        cnt += 7
    elif a[i] == 'P' or a[i] =='Q' or a[i] =='R' or a[i] =='S' :
        cnt += 8
    elif a[i] == 'T' or a[i] =='U' or a[i] =='V' :
        cnt += 9
    elif a[i] == 'W' or a[i] =='X' or a[i] =='Y' or a[i] =='Z' :
        cnt += 10
print(cnt)