// 2023/05/28/Sun 
// 백준 2750번 문제
// 2021112045 송우승
#include <stdio.h>
#define max 1000
int main()
{
    int n, tmp;
    int arr[max] = {0,};
    scanf("%d", &n);

    for(int i= 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    for(int i = 0; i < n; i++)
        for(int j = 0; j < n-1-i; j++)
        {
            if(arr[j] > arr[j+1])
            {
                tmp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = tmp;
            }
        }
  
    for(int i = 0; i < n; i++)
        printf("%d\n", arr[i]);
}