// 30007
// 2023-09-27 18:26:17
#include <stdio.h>
int main()
{
    int a,b,c;

    int n;

    scanf("%d",&n);

    for(int i = 0; i< n; i++)
    {
        scanf("%d %d %d", &a,&b,&c);
        printf("%d\n",a*(c-1)+b);
    }

}