// 2023/05/26/Fri 
// 백준 11047번 문제
// 2021112045 송우승
#include <stdio.h>
int main()
{
    int n, k, j, cnt = 0;
    int arr[100] = {0,}; 

    scanf("%d %d", &n, &k);
    j = n-1; // index of arr = 0 ~ n-1  
    for(int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    while(k > 0) 
    {
        if(arr[j] > k) j--; // ex ) if k = 4000, arr[n-1] = 5000 일 때 계산할 수 없으니 j-1을 함. 
        else {
            k -= arr[j]; // k를 j로 뺄 수 없을 때까지 반복 
            cnt++; // 동전 개수 count
        }
    }
    printf("%d\n",cnt);


    return 0;
}


