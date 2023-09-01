// 2744
// 230901
#include <stdio.h>
int main()
{
    char a[101];
    scanf("%s",a);
    for(int i = 0; i<101; i++)
    {

        if(a[i] >= 65 && a[i] <= 90)
        {
            a[i]+=32;
        }
        else if(a[i] >= 97 && a[i] <= 122)
        {
            a[i]-=32;
        }
    
    }
    printf("%s",a);
    
}