// 1212
// 23/08/27 

#include <stdio.h>
int main()
{
    int o;
    int n;
    int sum = 0;
    scanf("%d", &o);
    for(int i =0; i < o; i++)
    {
        scanf("%1d",&n); //1d를 쓰면 숫자 하나만 입력된다. 
        sum += n;
    }
    printf("%d",sum);
}