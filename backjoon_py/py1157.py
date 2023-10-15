#1157번 문제: 단어 공부

'''
s = input().upper()
s_list = list(set(s)) # 입력받은 문자열에서 중복값을 제거 -> 리스트로 변환, 그리고 set은 순서가 없으므로 다시 list로 변환
print(s_list)
cnt_list = []
for i in s_list:
    cnt  = s.count(i) # count 함수로 i가 문자열 s에 몇 개 있는지 확인하고 그 값을 cnt에 저장
    cnt_list.append(cnt) # count 숫자를 리스트에 append
if cnt_list.count(max(cnt_list)) > 1: # count 숫자 최대값이 중복되면
    print('?')
else:
    print(s_list[cnt_list.index(max(cnt_list))]) # cnt_list의 최대값 인덱스를 찾고 s_list의 해당 인덱스 문자 출력
'''

# set 함수를 사용하지 않고 풀기
s = input().upper()
arr = [0] * 26
for i in s:
    arr[ord(i)-65] += 1 # ord() 함수는 문자의 아스키 코드 값을 돌려주는 함수
if arr.count(max(arr)) > 1:
    print('?')
else:
    print(chr(arr.index(max(arr))+65)) # chr() 함수는 아스키 코드 값을 문자로 변환하는 함수
    # index() 함수는 리스트에 x 값이 있으면 x의 위치 값을 돌려주는 함수
    # 따라서 chr(arr.index(max(arr))+65)는 arr에서 최대값의 인덱스를 찾고 그 값을 아스키 코드로 변환한 후 문자로 변환
    

