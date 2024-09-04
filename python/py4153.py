# 4153 : 직각삼각형
while(1) :
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0 :
        break
    a = a**2 
    b = b**2 
    c = c**2 
    if (a + b == c) or (a + c == b) or (b + c == a) : 
    # 직각삼각형의 조건 : 가장 긴 변의 제곱 = 나머지 두 변의 제곱의 합
        print("right")
    else :
        print("wrong")
    
    