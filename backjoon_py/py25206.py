import sys
input = sys.stdin.readline

sum = 0
total_credit = 0 

for _ in range(20):
    name, credit, grade = input().split()

    credit = float(credit)

    if grade == 'P' :
        continue
    
    if grade == 'A+' :
        sum += (credit * 4.5)
        total_credit += credit
    elif grade == 'A0':
        sum += (credit * 4.0)
        total_credit += credit
    elif grade == 'B+':
        sum += (credit * 3.5)
        total_credit += credit
    elif grade == 'B0':
        sum += (credit * 3.0)
        total_credit += credit
    elif grade == 'C+':
        sum += (credit * 2.5)
        total_credit += credit
    elif grade == 'C0':
        sum += (credit * 2.0)
        total_credit += credit
    elif grade == 'D+':
        sum += (credit * 1.5)
        total_credit += credit
    elif grade == 'D0':
        sum += (credit * 1.0)
        total_credit += credit
    elif grade == 'F':
        total_credit += credit

total_grade = sum / total_credit


# 세가지 소숫점 슬라이싱 출력 방식 
print("{0:.6f}" .format(total_grade)) # format 방식 (0:은 format의 값 순서 번호다.)
#print(f'{total_grade:.6f}') # f-string 방식
#print("%.6f" %(total_grade)) # C언어 방식