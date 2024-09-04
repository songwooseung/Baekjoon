#include <stdio.h>
int main()
{
    char d = ' ';

    scanf("%c",&d);

    if(d == 'M') printf("MatKor");
    else if(d == 'W') printf("WiCys");
    else if(d == 'C') printf("CyKor");
    else if(d == 'A') printf("AlKor");
    else if(d == '$') printf("$clear");

}