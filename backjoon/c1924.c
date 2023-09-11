// 백준 1924 
// 2023-09-12 07:18:57
#include <stdio.h>
int main()
{
    int month[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
    char *day[7] = {"SUN","MON","TUE","WED","THU","FRI","SAT"}; 
    //case 0 -> SUN, case 1 -> MON --, case 6 -> SAT
 
    int x, y;
    scanf ("%d %d", &x, &y);

    for (int i = 0; i < x-1; i++)
    //if x = 1 break; -> cal y
    //if 2007/2/1 -> 31+1(month(1)+y) = 32 -> 32%7 == 4(THU)
        y += month[i];

    printf("%s",day[y%7]);
}