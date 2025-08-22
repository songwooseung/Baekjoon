import sys
input = sys.stdin.readline

# Counter나 enumerate로 빈도 수 측정 후 출력 가능, 이 라이브러리들을 쓰면 딕셔너리형태로 키,값 반환함
# 이 알고리즘을 통해 배운 것 -> 리스트 만들 때 [*map(int,input().split())] 이렇게 써도됨.


# 방법 1은 index를 쓰는 방법
''' 
# 숫자카드 N, M 입력
N = int(input())
n1 = list(map(int,input().split()))
M = int(input())
n2 = list(map(int,input().split()))

# M만큼 결과물을 담을 배열 
res = [0] * M

for i in n1 :
    if i in n2 :
        j = n2.index(i)
        res[j] += 1
    
# print(' '.join(map(str,res)))
print(*res)
'''

# 방법 2는 딕셔너리로 index안쓰고 출력하는 방법
'''
N = int(input())
n1 = list(map(int,input().split()))
M = int(input())
n2 = list(map(int,input().split()))

dic = {}

for i in n1 :
    if i in dic :
        dic[i]+=1
    else :
        dic[i] = 1

for i in n2 :
    if i in dic :
        print(dic[i], end=" ") # i키에 매핑되는 value값 출력
    else :
        print(0, end=" ") # n2에 해당없는 값도 출력해야 하므로

# 또는
# for target in n2:
#     result = dic.get(target) # get으로 해당 키의 빈도수 출력
#     if result == None:
#         print(0, end=" ")
#     else:
#         print(result, end=" ")
'''

# 방법 3 이분탐색
# 이분탐색은 정렬된 배열에서만 사용할 수 있다. 

def binarySearch(arr, target, start, end) :
    if start > end :
        return 0 
    
    mid = (start+end) // 2 # 정렬된 배열의 중앙값부터 시작

    if arr[mid] == target :
        return dic.get(target) # 키값에 매핑되는 값 출력, 없다면 0이 나오겠지
    elif arr[mid] < target :
        return binarySearch(arr,target,mid+1,end)
    else :
        return binarySearch(arr,target,start,mid-1) # start값은 재귀에 거듭할수록 그 전 start값을 그대로 가져감. 

N = int(input())
n1 = sorted(map(int,input().split()))
M = int(input())
n2 = list(map(int,input().split()))

dic = {}

for i in n1 :
    if i in dic :
        dic[i] += 1
    else :
        dic[i] = 1 
    
for target in n2 :
    print(binarySearch(n1,target,0,N-1),end=" ")

