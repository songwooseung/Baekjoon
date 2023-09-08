//백준 15552
//230819
#include <stdio.h>
int main()
{
    int n;
    int a,b;
    scanf("%d", &n);
    for(int i = 0; i < n; i++)
    {
        scanf("%d %d", &a,&b);
        printf("%d\n",a+b);
    }
}