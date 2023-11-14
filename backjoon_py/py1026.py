# 1026
import sys
input = sys.stdin.readline

# B 재배열을 무시하고 풀었을 때, a는 내림차순, b는 오름차순해서 풀이해주면 된다.
'''
def arr(n) : 
    S = [0] * n
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    a.sort(reverse=True)
    b.sort()
    for i in range(n):
        S[i] = a[i] * b[i]
    return print(sum(S))
'''

# 재배열 규칙을 지키고, 정석적으로 풀었을 때
def arr2(n, a, b) : 
    S = [0] * n 
    
    for i in range(n) :
        S[i] = min(a) * max(b) # a의 가장 작은 값, b의 가장 큰 값을 곱하고, 그 값들은 배열 S에 추가하고 pop을 사용해서 사용한 요소들을 제거하는 것을 반복한다. 
        a.pop(a.index(min(a))) # min(a)가 있는 인덱스 위치 -> 여기서 a.pop(int)는 인덱스 위치의 값을 없애는 것이므로 min(a)를 넣으면 안된다. 예로 a가 [1,2,3]일 때 a.pop(2)를 하면 a의 2번째 인덱스인 3이 제거된다.
        b.pop(b.index(max(b)))
    return sum(S)
        


if __name__ =="__main__" : 
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    result = arr2(n, a, b)
    print(result)    
