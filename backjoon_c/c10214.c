// 10214
// 2023-09-14 13:08:51
#include <stdio.h>
int main()
{
    int y;
    int k;
    int Test;
    scanf("%d",&Test);

    for(int i = 0; i < Test; i++)
    {
        int ysum = 0;
        int ksum = 0;
        for(int i = 0; i < 9; i++)
        {
            scanf("%d %d",&y,&k);
            ysum += y;
            ksum += k;
        }
        if(ysum > ksum) printf("Yonsei\n");
        else if(ysum < ksum) printf("Korea\n");
        else printf("Draw\n");
    }
    return 0;
}