#include <stdio.h>
int Partition(int r[], int low, int high){
	//对子序列r[low...high]进行一次划分, 并返回枢轴应当所处的位置
	//使得在枢轴之前的关键字均不大于它的关键字,枢轴之后的关键字均不小于它的关键字
	r[0] = r[low];
	while(low < high){
		while(low<high && r[high] >= r[0])
			high--;
		r[low] = r[high];
		while(low<high && r[low] <= r[0])
			low++;
		r[high] = r[low];
	} 
	r[low] = r[0];
	return low;
}

void QSort(int d[], int s, int t){
	//对子序列d[s..t]进行快速排序 
	int pivotloc;
	if(s < t){
		pivotloc = Partition(d, s, t);
		QSort(d, s, pivotloc-1);//注意这里是减一,对枢轴之前的序列递归快排 
		QSort(d, pivotloc+1, t);//对枢轴之后的序列递归快排 
	}
}

void QuickSort(int L[]){
	
}

int main(){
	int L1[8] = {0,42,30,68,98,86,15,57};
	QSort(L1, 1, 7);
	//printf("shuzhou : %d\n\n",Partition(L1, 1, 7));
	for(int i = 1; i < 8; i++)
		printf("%d\n", L1[i]);
}
