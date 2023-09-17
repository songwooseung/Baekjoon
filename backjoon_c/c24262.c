// 24262 (이 문제 오류인듯?)
// 2023-09-18 08:02:58
#include <stdio.h>
int main()
{
    long long int x,y;
    scanf("%lld %lld", &x,&y);
    printf("%lld",(x+y)*(x-y));
    return 0;
}