//브3
//백준 5073번
#include <stdio.h>
int main()
{
    int x,y,z;
    while(1)
    {
        scanf("%d %d %d",&x,&y,&z);
        if(x == 0 && y == 0 && z == 0) break;
        if(x==y && y == z && x == z) printf("Equilateral\n");
        else if(x >= y+z || y >= z + x || z >= x + y) printf("Invalid\n");
        else if((x==y && x != z) || (x == z && x != y) || (y==z && y != x)) printf("Isosceles\n");
        else if(x != y && y != z && z != x) printf("Scalene\n");
    }
}