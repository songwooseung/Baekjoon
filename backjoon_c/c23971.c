// 백준 23971
// 23/08/12
#include <stdio.h>
#include <math.h>
int main() // ctrl + /, alt + shift + A 주석 단축키 //
{
    int H, W, N, M, x, y; // 행, 열, 세로, 가로 순서
    int human = 0; // ceil로 올림한 값 곱해서 수용인원 구하기
    scanf("%d %d %d %d",&H, &W, &N, &M); 
    x = ceil((double)H/(N+1)); 
    //세로 줄 인원 구하기 -> N+1은 한칸 띄어 앉아야하기 때문, 
    //double에서 ceil하는 이유는 5/2 = 2.5일 때 소수 0.5는 버려지기 때문에 올리기 위함.
    y = ceil((double)W/(M+1)); 
    //이하동문
    human = x * y;
    printf("%d",human);
}