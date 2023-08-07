// 2023/05/19/Fri 
// 백준 2920번 문제
// 2021112045 송우승
#include <stdio.h>
int main(){
    int arr[8];
    int as = 0;
    int des = 0;

  
    for(int i = 0; i < 8; i++)
    {
        scanf("%d",&arr[i]);
        if(arr[i] == i+1)
        {
            as++;
        }
        else if(arr[i] == 8-i)
        {
            des++;
        }
    }
    if (as == 8) printf("ascending\n");
    else if (des == 8) printf("descending\n");
    else printf("mixed\n");

    return 0;

}
