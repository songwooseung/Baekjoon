import sys

arr = [0,0,0]
cnt = 0

for i in range(3):
    FB = sys.stdin.readline().strip() # 개행문자 제거 
    if FB.isdigit():
        arr[i] = int(FB)
        cnt = i

s = len(arr)-cnt

if (arr[cnt]+s) % 3 == 0 and (arr[cnt]+s) % 5 == 0 :
    print('FizzBuzz')
elif ((arr[cnt]+s) % 3 == 0 and (arr[cnt]+s) % 5 != 0):
    print('Fizz')
elif ((arr[cnt]+s) % 3 != 0 and (arr[cnt]+s) % 5 == 0):
    print('Buzz')
else : 
    print(arr[cnt]+s)
