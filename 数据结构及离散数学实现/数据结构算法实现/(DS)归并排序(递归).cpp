#include <stdio.h>

void Merge(int SR[], int TR[], int i, int m, int n) {//0,5,10
	//将相邻的有序区间SR[i.m]和SR[m+1,n]归并为有序的TR[i,n] 
	int a=i,b=m,c=i;
	while(a<m && b<n){
		if(SR[a] <= SR[b]){
			TR[c] = SR[a];
			a++;
			c++;
		}
		else{
			TR[c] = SR[b];
			b++;
			c++;
		}
	}
	for(a; a<m; a++){
		TR[c] = SR[a];
		c++;
	}
	for(b; b<n; b++){
		TR[c] = SR[b];
		c++;
	}
} 

void MSort(int R1[], int R2[], int i, int s, int t){//0,0,10
	void Merge(int SR[], int TR[], int i, int m, int n);
	//对R1[s..t]归并排序,若i%2==1, 则排序后的记录存入R2[s..t],否则存入R1[s..t]
	int m;
	if(s == t){
		if(1==i%2)
			R2[s] = R1[s];
	}
	else{
		m = (s+t)/2;
		MSort(R1, R2, i+1, s, m);
		MSort(R2, R1, i+1, m+1, t);
		if(1 == i%2)
			Merge(R1, R2, s-1, m, t);
		else
		 	Merge(R2, R1, s-1, m, t);
	}
}

void MergeSort(int L[], int n){
	void MSort(int R1[], int R2[], int i, int s, int t);
	//对数组长度为n的数组L进行归并排序
	int R[n];
	MSort(L, R, 0, 1, n-1); 
} 

int main(){
	int n = 10;
	int L1[10] = {12,30,68,98,186,15,57,69,76,79};
	int L2[10];
	//Merge(L1, L2, 0, 5, 10);1,5,10
	MSort(L1, L2, 0, 1, 10);
	//MergeSort(L1, n);
	for(int i=0; i<n; i++)
		printf("%d\n",L2[i]);
}
