# 5622
# 2023-10-07 07:45:45
cnt = 0
a = list(input())

'''
# 1번 방법
dial = ["ABC","DEF",'GHI',"JKL","MNO","PQRS","TUV","WXYZ"]
for i in a: # 반복문이므로 0번째 방부터 하나하나 넣는다?
    for j in dial : # 방 0~7까지 넣고 if문 비교, break가 없으니 끝까지 비교
        if i in j : 
            cnt += dial.index(j) + 3
print(cnt)

# for i in a는 리스트 a에 있는 값들을 i에 하나하나 순서대로 옮겨서 사용하는 것이다. 
'''
    
'''
# 2번 방법
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
'''

'''
# 틀린 정답 
# or 뒤의 'B' or 'C'는 a[i]와 비교되지 않고 별도의 조건으로 간주되므로 항상 참으로 간주된다. 
# 그렇기 때문에, elif로 넘어가기 전에 'B', 'C'로 인해 ABC가 포함되지 않아도 참으로 보고 반복문이 끝날 때까지 cnt += 3이 되는 것이다.
for i in range(len(a)) :
    if a[i] == 'A' or 'B' or 'C' :
        cnt += 3
    elif a[i] == 'D' or 'E' or 'F' :
        cnt += 4
    elif a[i] == 'G' or 'H' or 'I' :
        cnt += 5
    elif a[i] == 'J' or 'K' or 'L' :
        cnt += 6
    elif a[i] == 'M' or 'N' or 'O' :
        cnt += 7
    elif a[i] == 'P' or 'Q' or 'R' or 'S' :
        cnt += 8
    elif a[i] == 'T' or 'U' or 'V' :
        cnt += 9
    elif a[i] == 'W' or 'X' or 'Y' or 'Z' :
        cnt += 10
print(cnt)
'''