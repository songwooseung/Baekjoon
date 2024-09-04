t = int(input())
for i in range(t):
    N, M = map(int,input().split())
    # N은 모든 닭의 다리수의 합
    # M은 모든 닭의 수 
    # 이 중에 다리가 잘린 닭의 수와 멀쩡한 닭의 수를 구해야한다.
    # 닭의 다리는 2개니까 N= 5 M = 3이면 다리가 잘린 닭의 수는 1이고, 멀쩡한 닭의 수는 2이다.

    A = (M*2) - N 
    B = N-M
    print(A,B)
    
    
    
    