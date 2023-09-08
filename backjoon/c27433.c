// 27433
// 230831
#include <stdio.h>
int main()
{
    int n;
    int cnt = 0;
    long long s;
    scanf("%d",&n);
    if(n == 0){
        printf("1");
        return 0;
    }
    s = n;
    for(int i=n-1; i>0; i--)
    {
        s = s*i;
    }
    
    printf("%lld",s);
}