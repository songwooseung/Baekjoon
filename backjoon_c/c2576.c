//백준 2576
//브3, 23/08/13
#include <stdio.h>

int main() {
    int sum = 0;
    int num[7];
    int hol[7];
    int k = 0;
    int min = 100;

    for (int i = 0; i < 7; i++) {
        scanf("%d", &num[i]);
        if (num[i] % 2 == 1) {
            sum += num[i];
            hol[k] = num[i];
            k++;
        }
    }

    if (k > 0) { // 홀수가 하나라도 있을 경우
        for (int i = 0; i < k; i++) {
            if (min > hol[i]) 
                min = hol[i];
        }
        printf("%d\n%d", sum, min);
    } else 
        printf("-1");

    return 0;
}