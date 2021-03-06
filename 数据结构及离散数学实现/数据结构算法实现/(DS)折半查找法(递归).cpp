#include <stdio.h>

int BinSearch(int r[], int key, int low, int high){
	int mid = (low + high)/2;
	if(r[mid] == key)
		return mid;
	if(low > high)
		return NULL;
	if(r[mid] < key)
		BinSearch(r, key, mid+1, high);
	else
		BinSearch(r, key, low, mid-1);
}

int main(){
	int rcd[10] = {12,24,25,28,40,45,49,50,58,60};
	printf("search elem: %d\n",BinSearch(rcd, 28, 0, 9));
}
