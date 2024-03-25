# https://ctkim.tistory.com/entry/Python-%EC%9E%85%EB%AC%B8-%EA%B0%95%EC%A2%8C-12-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A7%91%ED%95%A9Set-%EC%A0%95%EB%A6%AC-%EB%B0%8F-%EC%82%AC%EC%9A%A9%EB%B2%95
import sys
input = sys.stdin.readline

N, G = map(str,input().split())
N = int(N)

game = set()

for i in range(N): # 집합은 add할 때 입력받으면 \n까지 포함된다. 
    game.add(input().rstrip("\n"))

human = len(game)

# 임스를 포함한 게임 인원 
if G == "Y":
    print(human)
elif G == "F":
    print(human//2)
elif G == "O":
    print(human//3)
else :
    print("잘 못 입력")