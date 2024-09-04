// 30087
// 2023-09-25 13:16:33
// strcmp를 사용하여 문자열을 비교 하여 출력하기 
#include <stdio.h>
#include <string.h>
int main(){
    int n;
    char c[100];
    scanf("%d",&n);

    for(int i = 0; i < n; i++)
    {
        scanf("%s",c);
        if(!strcmp(c,"Algorithm")) printf("204\n");
        else if(!strcmp(c,"DataAnalysis")) printf("207\n");
        else if(!strcmp(c,"ArtificialIntelligence")) printf("302\n");
        else if(!strcmp(c,"CyberSecurity")) printf("B101\n");
        else if(!strcmp(c,"Network")) printf("303\n");
        else if(!strcmp(c,"Startup")) printf("501\n");
        else printf("105\n");
        
    }
}
