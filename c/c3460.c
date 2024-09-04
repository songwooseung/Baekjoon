// 3460
// 2023-10-02 17:53:56

#include <stdio.h>
int main()
{
    int t, n;
    scanf("%d", &t);
    
    for(int i = 0; i < t; i++)
    {
        int cnt = 0;
        scanf("%d", &n);

        while(n != 0)
        {
            if (n % 2 == 1) printf("%d ",cnt);
            n /= 2;
            cnt ++;
        }
        printf("\n");
    }
}