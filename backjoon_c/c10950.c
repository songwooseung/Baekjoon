// 10950
// 20230823

#include <stdio.h>
int main()
{
    int n;
    int x, y;

    scanf("%d",&n);

    for(int i = 0; i < n; i++)
    {
        scanf("%d %d", &x,&y);
        printf("%d\n",x+y);
    }
}