N = int(input())
for i in range(N):
    c = []
    c = input()
    
    len_c = len(c)
    
    if(len_c >= 6 and len_c <= 9):
        print("yes")
    else:
        print("no")