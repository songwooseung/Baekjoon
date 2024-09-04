# 1057 : 나누기

N = int(input())
F = int(input())
N = N - N % 100
while(N % F != 0):
    N += 1

print(str(N)[-2:]) # n이 1002일 때, 이를 문자열로 바꾸고 뒤에서 두번째 자리까지 출력한다.