#include <stdio.h>

int main(void) {
	int x,y,j;
	scanf("%d%d",&x,&y);
	for(j=x+1;j<=y;j++)
	{
	if(j%2!=0)
            printf("%d ",j);
	}
	return 0;
}
