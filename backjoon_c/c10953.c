// 10953
// 2023-09-11 07:19:58
#include <stdio.h>
int main()
{
    int num;
    scanf("%d",&num);
    int x,y;
    for(int i = 0; i < num; i++)
    {
        scanf("%d,%d",&x,&y);
        printf("%d\n",x+y);
    }
}