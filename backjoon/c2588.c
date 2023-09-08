// 2588
// 2023-09-08 11:49:03
#include <stdio.h>
int main()
{
    int a,b;
    int sum;
    scanf("%d %d",&a,&b);
    int hap;
    sum = a*b;
    while(b > 0)
    {
        hap = a*(b%10);
        printf("%d\n",hap);
        b /= 10;
    }
    printf("%d",sum);
}