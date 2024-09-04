//5717
//2023-09-15 11:29:32
#include <stdio.h>
int main()
{
    int a,b;

    while(1)
    {
        scanf("%d %d", &a,&b);
        if(a == 0 && b ==0) break;
        else printf("%d\n",a+b);
    }
    return 0;
}