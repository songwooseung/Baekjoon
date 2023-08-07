// 2023/06/06/TUE 
// 백준 2587번 문제
// 2021112045 송우승
#include <stdio.h>
#define swap(a, b) {int temp = a; a=b; b=temp;}
int main()
{
    int avg = 0;
    int arr[1001] = {0,};
    for(int i = 0; i < 5; i++)
    {
        scanf("%d",&arr[i]);
        avg += arr[i];
    }   
    avg /= 5;
    for(int i = 0; i < 5; i++)
        for(int j = 0; j < 5-i-1; j++)
        {
            if(arr[j] > arr[j+1]) swap(arr[j], arr[j+1]);
        }

    printf("%d\n%d",avg,arr[2]);
}





