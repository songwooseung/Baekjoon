// 2476
// 2023-10-04 07:57:03
#include <stdio.h>
int main()
{
    int n;
    int a,b,c;
    int price[1000];
    int max, mp = 0;
    scanf("%d",&n);

    for(int i = 0; i < n; i++)
    {
        scanf("%d %d %d",&a,&b,&c);
        if(a == b && a == c && b == c)
            price[i] = 10000+(a*1000);
        else if (a == b || a == c)
            price[i] = 1000+(a*100);
        else if (b == c)
            price[i] = 1000+(b*100);
        else{
            if(a > b && a > c)
                max = a;
            else if(b > a && b > c)
                max = b;
            else if(c > a && c > b)
                max = c;
            price[i] = max * 100;
        }
        if(price[i] > mp)
            mp = price[i];
    }
    printf("%d", mp);
}