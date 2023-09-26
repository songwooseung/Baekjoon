//9086
//2023-09-26 21:26:05

#include <stdio.h>
#include <string.h>

int main()
{
    char c[1001];
    int num;
    scanf("%d",&num);

    for(int i = 0; i <num; i++)
    {
        scanf("%s",c);
        printf("%c%c\n",c[0],c[strlen(c)-1]);
    }
}