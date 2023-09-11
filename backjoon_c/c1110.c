// 2023/05/20/SAT 
// 백준 1110번 문제
// 2021112045 송우승
#include <stdio.h>
int main(){
    int num, result; 
    int a,b,c,d;
    int cnt = 0;

    scanf("%d",&num);
    result = num; 

    while(1)
    {
        a = num / 10; 
        b = num % 10; 
        c = (a+b) % 10; // 맨 오른쪽 값으로 이어 붙여야하니까 %해줌.
        d = (b*10) + c;
        num = d; 
        cnt ++; 

        if (result == num) break;
    }
    printf("%d\n", cnt);
}
