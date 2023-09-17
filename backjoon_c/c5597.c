// 5597
// 2023-09-17 15:16:51
#include <stdio.h>
int main()
{
    int arr[31] = {0,};
    int num;
    for(int i = 0; i < 28; i++)
    {
        scanf("%d", &num);
        arr[num] = 1;
    }
    for(int i = 1; i <= 30; i++)
    {
        if(arr[i] == 0)
        {
            printf("%d\n",i); //주소 값을 나타내는 게 아니라 해당 인덱스를 출력
        }
    }
    
}