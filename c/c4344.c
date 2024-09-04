// 4344
// 2023-10-03 19:08:27

#include <stdio.h>
int main()
{
    int C, N;
    scanf("%d",&C);
    
    for(int i = 0; i < C; i++)
    {
        scanf("%d", &N);
        int score[1000];
        int sum = 0;   
        double avg = 0.0;
        int cnt = 0;
        for(int j =0; j < N; j++)
        {
            scanf("%d",&score[j]);
            sum += score[j];
        }
        avg = (double)sum / N;
        
        for(int k = 0; k < N; k++)
        {
            if(avg < score[k]) cnt++;
        }
        printf("%.3lf%%\n",((double)cnt*100)/N);
    }
    return 0;
    
}