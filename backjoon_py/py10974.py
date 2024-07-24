import sys
input = sys.stdin.readline

N = int(input())
seq = []


def back():

    if len(seq) == N :
        return print(*seq)


    for i in range(1, N+1):
        if i not in seq : 
            seq.append(i)
            back()
            seq.pop()
    
back()

    