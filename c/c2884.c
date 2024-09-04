// 2884
// 2023-09-21 13:04:21
#include <stdio.h>
int main()
{
    int h,m;

    scanf("%d %d", &h,&m);

    if (m >= 45)
    {
        m -= 45;
        printf("%d %d", h,m);
    
    }
    else
    {
        h -=  1;
        if (h < 0) h = 23;
        m = (60 - 45) + m;
        printf("%d %d", h,m);
    }
}