// 2577
// 2023-09-07 20:29:11
#include <stdio.h>
int main()
{
    int a,b,c,sum,num;
    scanf("%d",&a);
    scanf("%d",&b);
    scanf("%d",&c);
    sum = a*b*c;
    int temp[10] = {0,};

    while(sum > 0)
    {
        num = sum%10;
        temp[num]++;
        sum /= 10;
    }
    for(int i = 0; i < 10; i++)
    {
        printf("%d\n", temp[i]);
    }
}