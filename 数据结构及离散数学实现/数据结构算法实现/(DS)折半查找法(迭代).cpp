#include <stdio.h>

int BinSearch_ite(int r[], int key, int low, int high){
	int mid;
	while(low <= high){
		mid = (low+high)/2;
		if(r[mid] == key)
			return mid;
		else if(r[mid] > key)
			high = mid-1;
		else
			low = mid+1;
	}
	return -1;
} 

int main(){
	int rcd[10] = {12,24,25,28,40,45,49,50,58,60};
	printf("search elem: %d\n",BinSearch_ite(rcd, 28, 0, 9));
}
