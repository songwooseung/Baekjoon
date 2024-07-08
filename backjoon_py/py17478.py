import sys
N = int(sys.stdin.readline())
def fn(n):
    under_bar = '____' * n
    if n == N :
        print(f'{under_bar}"재귀함수가 뭔가요?"')
        print(f'{under_bar}"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(f'{under_bar}라고 답변하였지.')
        
        # 1. return 을 해두지 않으면 fn(n+1)로 인해 무한 루프로 돌아감.
        # 2. return으로 인해 fn(n+1)이 수행 종료되어 밑 줄로 이동함.
        # 즉 return은 함수의 종료를 나타냄.
        return  
    
    print(f'{under_bar}"재귀함수가 뭔가요?"')
    print(f'{under_bar}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print(f'{under_bar}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print(f'{under_bar}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')

    fn(n+1) 

    print(f'{under_bar}라고 답변하였지.')

print(f'어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
fn(0)
