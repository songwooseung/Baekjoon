// 2023/06/01/WED
// 백준 11399번 문제
// 2021112045 송우승
#include <stdio.h>
#define swap(a, b) {int temp = a; a=b; b=temp;}
#define max 1001
int main()
{
    int num, sum = 0;
    int arr[max] = {0,};
    
    scanf("%d", &num);

    for(int i = 0; i < num; i++)
        scanf("%d",&arr[i]);

    for(int i = 0; i < num; i++)
        for(int j = 0; j < num-1-i; j++)
        {
            if(arr[j] > arr[j+1])
            {
                swap(arr[j], arr[j+1]);
            }
        }
    
    for(int i = 0; i < num; i++)
        sum += arr[i] * (num-i);

    printf("%d\n5", sum);
    return 0;
}