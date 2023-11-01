# 11719
while True : 
    try:
        print(input()) # 입력받은 그대로 출력
    except EOFError: # EOFError 발생 시 반복문 탈출
        break
    