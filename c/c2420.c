// 2420
// 2023-09-29 13:09:20
#include <stdio.h>
#include <stdlib.h>
int main()
{
    long long int a, b;
    scanf("%lld %lld", &a,&b);
    
    if(a < b) printf("%lld",b-a);
    else printf("%lld",a-b);
}