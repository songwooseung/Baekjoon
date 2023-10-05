// 2908
// 2023-10-05 13:50:52
#include <stdio.h>
int main()
{
    int A,B;
    int rev_A = 0, rev_B = 0;
    int reminder_A, reminder_B;
    scanf("%d %d", &A,&B);

    while(A != 0){
        reminder_A = A % 10; // ex) t1.734 -> 4반환, t2.73 -> 3반환
        reminder_B = B % 10; // t1.893 -> 3반환, t3.89 -> 9반환
        rev_A = (rev_A*10) + reminder_A; // t1.0*10+4 = 4이므로 rev_A엔 4가 들어간다. t2.4*10+9 = 49이므로 rev_A = 49
        rev_B = (rev_B*10) + reminder_B; // 위와 동일한 방식
        A /= 10;
        B /= 10;
    }
    if(rev_A > rev_B) printf("%d",rev_A);
    else if(rev_A < rev_B) printf("%d",rev_B);
    else printf("==");

}