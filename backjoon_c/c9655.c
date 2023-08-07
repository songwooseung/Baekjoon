// 2023/05/26/Fri 
// 백준 9655번 문제
// 2021112045 송우승
#include <stdio.h>
int main()
{
    int n; 
    scanf("%d", &n);

    if(n % 2 == 1) // 1 or 3 이기 때문에 -> 홀수 승 : SK , 짝수 승 : CY
        printf("SK");
    else 
        printf("CY");
    return 0;
}