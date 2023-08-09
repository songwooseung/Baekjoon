//백준 4101
#include <stdio.h>
int main()
{
    int n, f;
    while(1)
    {
        scanf("%d %d",&n,&f);
        if(n>f) printf("Yes\n");
        else if(n > 0 && n <= f) printf("No\n");
        else break;
    } 

}
