import sys

N = int(sys.stdin.readline())
member = []
for i in range(N):
    age, name = map(str,sys.stdin.readline().split())
    member.append((int(age),name))

member.sort(key=lambda x : x[0])

# ------------------------------
for members in member : 
    print(members[0],members[1])

'''
for i in range(N):
    print(member[i][0],member[i][1])
'''