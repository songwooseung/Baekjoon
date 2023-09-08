// 10952
// 2023-09-04 20:51:17
#include <stdio.h>
int main()
{
    int a,b;
    while(1)
    {
        scanf("%d %d", &a,&b);
        if(a!=0 || b!= 0)
            printf("%d\n",a+b);
        else break;
    }
    return 0;
}