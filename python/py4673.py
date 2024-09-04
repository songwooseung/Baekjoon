import time
start = time.time()

num = set(range(1,10001))
num2 = set()

for i in range(1,10001):
    s = i
    for j in str(i):
        s += int(j)

    num2.add(s)
        
# set은 순서가 없기 때문에, 값에 대응되는 것만 빼주면된다. 
num = sorted(num-num2)
    
for i in num :
    print(i)
print(f"{time.time()-start:.4f} sec")

# 결론 set은 존나 빠르다. 