//백준 2562
//230814 
#include<stdio.h>
int main()
{
    int num[9];
    int max = 0;
    int area;
    for (int i = 0; i < 9; i++)
    {
        scanf("%d",&num[i]);
    }
    for (int i = 0; i < 9; i++)
    {
        if(max < num[i])
        {
            max = num[i];
            area = i;
        } 
    }
    printf("%d\n%d", max, area+1);
    return 0;
}