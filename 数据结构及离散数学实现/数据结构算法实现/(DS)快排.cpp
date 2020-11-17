#include <stdio.h>
int Partition(int r[], int low, int high){
	//��������r[low...high]����һ�λ���, ����������Ӧ��������λ��
	//ʹ��������֮ǰ�Ĺؼ��־����������Ĺؼ���,����֮��Ĺؼ��־���С�����Ĺؼ���
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
	//��������d[s..t]���п������� 
	int pivotloc;
	if(s < t){
		pivotloc = Partition(d, s, t);
		QSort(d, s, pivotloc-1);//ע�������Ǽ�һ,������֮ǰ�����еݹ���� 
		QSort(d, pivotloc+1, t);//������֮������еݹ���� 
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
