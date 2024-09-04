// 15652
// 2023-09-19 07:43:18
#include <stdio.h>

int main() {
    int n; // 임스가 계획한 일수
    scanf("%d", &n);
    int planned_pages[n]; // 임스가 공부하고자 계획한 페이지 수 배열
    int actual_pages[n]; // 임스가 실제로 공부한 페이지 수 배열
    int cnt = 0; // 계획을 성실히 지킨 횟수

    // 임스가 공부하고자 계획한 페이지 수 입력
    for (int i = 0; i < n; i++) {
        scanf("%d", &planned_pages[i]);
    }

    // 임스가 실제로 공부한 페이지 수 입력
    for (int i = 0; i < n; i++) {
        scanf("%d", &actual_pages[i]);
    }

    // 각 날짜별로 계획을 성실히 지켰는지 확인
    for (int i = 0; i < n; i++) {
        if (actual_pages[i] >= planned_pages[i]) {
            cnt++; // 계획을 성실히 지켰으면 cnt 증가
        }
    }

    printf("%d", cnt); // 계획을 성실히 지킨 횟수 출력

    return 0;
}

// 배열의 index는 n까지로 하고, 나머지 두 배열의 값은 1~100까지의 수만 넣는다.