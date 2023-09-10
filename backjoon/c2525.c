//2525
//2023-09-10 13:41:46
#include <stdio.h>
int main()
{
    int hour, min;
    int A,B,C;

    scanf("%d %d", &A,&B);
    scanf("%d", &C);

    if((B+C) >= 60)
    {
        hour = (B+C) / 60;
        min = (B+C) % 60;
        if((A+hour) >= 24)
            printf("%d %d", (A+hour)-24, min);
        else
            printf("%d %d", A+hour, min);
    }
    else 
    {
        hour = A;
        min = B+C;
        printf("%d %d", hour, min);

    }
}