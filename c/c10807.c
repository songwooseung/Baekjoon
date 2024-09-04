// 백준 10807
// 230822
#include <stdio.h>
int main()
{
    int n, v;
    int cnt = 0;
    int num[101];

    scanf("%d",&n);

    for(int i = 0; i < n; i++)
    {
        scanf("%d",&num[i]);
        
    }
    
    scanf("%d",&v);

    for(int i = 0; i < n; i++)
    {
        if(num[i] == v) cnt++;
    }
    printf("%d", cnt);
}