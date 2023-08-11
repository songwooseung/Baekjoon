//백준 2309
//브1
#include <stdio.h>
int main()
{
    int sum = 0;
    int dwf[9];
    int dwf2[9];
    int over;
    int f1, f2;
    for(int i = 0; i < 9; i++)
    {
        scanf("%d", &dwf[i]);
        sum += dwf[i];   
    }
    
    over = sum - 100;

    for(int i = 0; i < 9; i++)
        for(int j = i+1; j < 9; j++)
        {
            if(over == (dwf[i] + dwf[j]))
            {
                f1 = dwf[i];
                f2 = dwf[j];
                break;
            }
        }

    int k = 0;
    for(int i = 0; i< 9; i++)
    {
        if(dwf[i] != f1 && dwf[i] != f2)
        {
            dwf2[k] = dwf[i];
            k++;
        }
    }

    int temp; 
    for(int i = 0; i < 7; i++)
        for(int j = i+1; j < 7; j++)
        {
            if(dwf2[i] > dwf2[j])
            {
                temp = dwf2[i];
                dwf2[i] = dwf2[j];
                dwf2[j] = temp;
            }
        }
    for(int i = 0; i < 7; i++)
        printf("%d\n",dwf2[i]);
}