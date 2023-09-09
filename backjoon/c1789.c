// 1789
// 2023-09-09 11:34:52

#include <stdio.h>
int main()
{
    long long int input, S = 0, N = 0;; // 4,294,967,295는 int 범위로 나타낼 수 없기 때문.

    scanf("%d",&input);

    while(1)
    {
        N++;
        S += N;

        if(S > input)
        {
            N--; // 자연수의 합이 input 값을 넘어가면 N-1을 해주고 반복문을 탈출한다.
            break;
        }
    }
    printf("%d",N);
}