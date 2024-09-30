# 배열을 만들어 합에 해당하는 수의 개수를 카운트하는 문제 풀이
import sys 
input = sys.stdin.readline

N = int(input())

# 코드 설명 : num_list에 N개의 조합을 각각 더해서 sum_list의 인덱스에 넣고 1을 집어 넣어 카운트하기 (시간 초과 최소화)

roma = [1, 5, 10, 50]
num_list = [] 
sum_list = [0] * 1001 # L * 20시 1000까지 나오므로 리스트 크기를 1001로 초기화


def back(depth, num): # depth == k
    if depth == N :
        sum_list[sum(num_list)] = 1
        return
    for i in range(num,4):
        num_list.append(roma[i])
        # print(num_list)
        back(depth+1,i) # 항상 자기 자신 index 이상 부터
        num_list.pop()

back(0,0)

print(sum(sum_list))

# SET을 이용한 문제 풀이
''' 
import sys
input = sys.stdin.readline

N = int(input())
S = set()

roma = [1,5,10,50]
arr = []

def back(k,num):
    if N == k :
        S.add(sum(arr)) 
        return 

    for i in range(num,4):
        arr.append(roma[i])
        back(k+1,i)
        arr.pop()

back(0,0)
print(len(S))
'''
