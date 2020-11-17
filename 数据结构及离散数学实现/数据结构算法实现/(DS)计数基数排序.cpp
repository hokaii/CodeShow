#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int ReturnRadix(int num, int digit){
	int i, j, number;
	i = num % (int)pow(10, digit+1);
	j = num % (int)pow(10, digit);
	return (i-j)/pow(10, digit);
}

void RadixPass(int rcd[], int rcd1[], int n, int i, int count[], int pos[]){
	int j, k ;
	for(j=1; j<=n; j++)
		count[ReturnRadix(rcd[j], i)]++;
	pos[0] = 1;
	for(j=1; j<10; j++)
		pos[j] = pos[j-1]+count[j-1];
	for(j=1; j<=n; j++){
		k = ReturnRadix(rcd[j], i);
		rcd1[pos[k]++] = rcd[j];
	}
}

void RadixSort(int rcd[], int n, int digitNum){//数组， 长度， 关键字位数 
	int rcd1[n], count[10], pos[10];
	int i = 0, j;
	while(i < digitNum){
		for(j=0; j<10; j++)
			count[j] = 0;
		if(0 == i%2)
			RadixPass(rcd, rcd1, n, i++, count, pos);
		else
			RadixPass(rcd1, rcd, n, i++, count, pos);
	}
	if(1 == digitNum%2)
		for(j=1; j<=n; j++)
			rcd[j] = rcd1[j];
} 

int main(){
	int a = 237;
	int rcd[9] = {0,337,332,132,267,262,164,260,167};
	printf("0: %d\n", ReturnRadix(a, 0));
	printf("1: %d\n", ReturnRadix(a, 1));
	printf("2: %d\n", ReturnRadix(a, 2));
	printf("3: %d\n", ReturnRadix(a, 3));
	RadixSort(rcd, 9, 3);
	for(int i=0;i<9;i++)
		printf("%d, ",rcd[i]);
}
