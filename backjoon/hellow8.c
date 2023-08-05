// 2023/06/05/MON
// 백준 2752번 문제
// 2021112045 송우승

#include <stdio.h>
int main()
{
    int num1 = 0, num2 = 0, num3 = 0;
    scanf("%d %d %d", &num1, &num2, &num3);
    if(num1 > num2)
        if(num1 > num3)
            if(num2 > num3) printf("%d %d %d ", num3,num2,num1);
                else printf("%d %d %d ", num2,num3,num1);
    if(num2 > num1)
        if(num2 > num3)
            if(num1 > num3) printf("%d %d %d ", num3,num1,num2);
                else printf("%d %d %d ", num1,num3,num2);
    if(num3 > num1)
        if(num3 > num2)
            if(num2 > num1) printf("%d %d %d ", num1,num2,num3);
                else printf("%d %d %d ", num2,num1,num3);
}