#include <stdio.h>
#define TRUE 1
#define FALSE 0
void BubbleSort(int a[] ,int n){
	int i, j, temp;
	for(i=n-1; i>0; i--){
		for(j=0; j<i; j++)
		if(a[j] > a[j+1]){
			temp = a[j];
			a[j] = a[j+1];
			a[j+1] = temp;
		}
	}
} 

void NewBubbleSort(int a[], int n){
	int i, j, temp;
	bool change = TRUE;
	for(i=n-1; i>1 && change; --i){
		change = FALSE;
		for(j=0; j<i; ++j)
			if(a[j] > a[j+1]){
				temp = a[j];
				a[j] = a[j+1];
				a[j+1] = temp;
				change = TRUE;
			}
	}
}

int main(){
	int a[10] = {3,10,43,65,34,76,123,54,23,32};
	int b[10] = {3,10,43,65,34,76,123,54,23,32};
	BubbleSort(a, 10);
	NewBubbleSort(b, 10);
	for(int i=0; i<10; i++){
		printf("%d, ", a[i]);
	}
	printf("\n");
	for(int i=0; i<10; i++){
		printf("%d, ", b[i]);
	}
}
