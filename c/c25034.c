// 25034
// 2023-09-12 07:12:56
#include <stdio.h>
int main()
{
    int goal;
    int num;
    int sum = 0;
    int x,y;

    scanf("%d",&goal);
    scanf("%d",&num);

    for(int i= 0; i < num; i++)
    {
        scanf("%d %d", &x,&y);
        sum += (x*y);
    }
    if(sum == goal) printf("Yes");
    else printf("No");
    return 0;
}