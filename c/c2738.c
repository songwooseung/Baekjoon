// 2738
// 2023-09-22 12:41:17

#include <stdio.h>
int main()
{
    int n, m;
    
    scanf("%d %d", &n,&m);

    int arr[100][100] = {0,};
    int arr2[100][100] = {0,};

    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
        {
            scanf("%d",&arr[i][j]);
        }
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
        {
            scanf("%d",&arr2[i][j]);
        }
    
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
        {
            arr[i][j] += arr2[i][j];
        }

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
}