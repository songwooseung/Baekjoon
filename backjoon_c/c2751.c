// 백준 2751
// 230819

#include <stdio.h>
#include <stdlib.h>


int compare(const int *a, const int *b){
    if(*(int*)a > *(int*)b) // 더블 포인터는 싱글 포인터의 주소값을 저장하기 때문에 둘을 더블 포인터로 비교한다.
        return 1; // 첫 번째 인자가 더 큰 경우, 두 값을 교환하여 더 작은 값을 앞으로 보낸다. (오름차순) 
    else if(*(int*) a < *(int*)b)
        return -1; // 두 번째 인자가 더 큰 경우, 두 값을 교환하지않고 그대로 둔다. (오름차순을 위해서 더 작은 값을 앞으로)
    else return 0; // 두 값이 같은 경우 퀵소트의 정확한 순서를 나타내기 위해 0을 반환하면 상대적 순서가 변하지 않는다.
}
int main()
{
    int *arr =NULL;
    int n;

    scanf("%d", &n); 
    arr = (int*)malloc(sizeof(int)*n); 

    for(int i = 0; i < n; i++) 
        scanf("%d",&arr[i]);
    
    qsort(arr, n, sizeof(int), compare);

    for(int i = 0; i < n; i++) 
        printf("%d\n", arr[i]);
    
    free(arr);

    return 0;
}