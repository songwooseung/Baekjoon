//백준 1094번 
#include<stdio.h>
int main()
{
    int N = 64;
    int X;
    int cnt = 0;
    scanf("%d", &X);

    while(X>0) // 붙일 수 있을 때까지
    {
        if(N > X)  
            N/=2; 
        else 
        {
            cnt++;
            X -= N;
        }
    }
    printf("%d", cnt);
}