# 2675
# 2023-10-14 15:14:26
t = int(input())

for i in range(t):
    arr = []
    string = [] 
    arr = list(input()) # 2 ABC -> ['2','','A','B','C']
    arr = ' '.join(arr).split()
    # join은 문자를 연결하여 문자열로 만듬
    # split은 문자열을 분리함.
    # 1. ' '.join -> ["2  A B C"] - 문자 사이에 공백이 추가됨. 여기서 원래 공백에는 추가 공백이 생긴다.
    # 2. split() default 공백 -> ['2','A','B','C'] - split은 연속된 공백도 하나의 공백으로 취급한다.
    # 따라서 ' '.join(arr).split()문은 같이 사용하는 경우는 리스트 내 불필요한 공백 요소를 제거하기 위해 사용한다.
    
    print(arr)
    # join함수는 문자열 합치기 
    # split은 나누기
    n = int(arr[0])
    for j in range(1,len(arr)):
        print(arr[j]*n,end="")
    print()
    
        
        
    
    