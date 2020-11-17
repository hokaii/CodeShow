#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1

typedef int RcdType;
typedef int KeyType;
typedef struct{
	RcdType *rcd;//�ѻ�ַ,0�ŵ�Ԫ���� 
	int n;//�ѳ��� 
	int size;//������ 
	int tag; //С���Ѻʹ󶥶ѵı�־, tag=0ΪС����,tag=1Ϊ�󶥶� 
	int (*prior)(KeyType, KeyType); //��������,���ڹؼ������ȱȽ� 
} Heap; //������ 

int greatPrior(int x, int y){
	//�󶥶����Ⱥ��� 
	return x>=y;
} 

int lessPrior(int x, int y){
	//С�������Ⱥ��� 
	return x<=y;
}

int InitHeap(Heap &H, int size){
	H.rcd = (RcdType*)malloc(size*sizeof(RcdType));
	if(H.rcd == NULL)
		return ERROR;
	H.size = size;
	return OK;
}

void MakeHeap(Heap &H, RcdType *E, int n, int tag, int(*prior)(KeyType, KeyType)){
	//��E������Ϊn�Ķ�H, ����Ϊsize, ��tagΪ0��1ʱ�ֱ��ʾС���Ѻʹ󶥶� 
	void ShiftDown(Heap &H, int pos);
	int i;
	for(i=1;i<=n;i++)
		H.rcd[i] = E[i];
	H.n = n;
	H.tag = tag;
	H.prior = prior;
	for(i=n/2;i>0;i--)
		ShiftDown(H, i);
}

int DestroyHeap(Heap &H){
	//���ٶ�H 
	for(int i=H.n; i>=0; i--){
		free(&(H.rcd[i]));
	}
	free(&H);
	return OK;
}

int SwapHeapElem(Heap &H, int i, int j){
	//������H�еĵ�i�����͵�j�����
	RcdType t;
	if(i<=0 || j<=0 || i>H.n || j>H.n)
		return ERROR;
	t = H.rcd[i];
	H.rcd[i] = H.rcd[j];
	H.rcd[j] = t;
	return OK;
} 

void ShiftDown(Heap &H, int pos){//�� 
	//�Զ�H��λ��Ϊpos�Ľ����ɸѡ,����posΪ������������Ϊ�Ӷ�
	int c, rc;
	while(pos <= H.n/2){
		c = pos*2;
		rc = pos*2+1;
		if(rc<=H.n && H.prior(H.rcd[rc], H.rcd[c]))
			c = rc;
		if(H.prior(H.rcd[pos], H.rcd[c]))
			return ;
		SwapHeapElem(H, pos, c);
		pos = c;
	}
}

int InsertHeap(Heap &H, RcdType e){
	//��e����� 
	int curr;
	curr = H.n+1;
	H.n++;
	if(curr > H.size)
		return ERROR;
	H.rcd[curr] = e;
	while(curr!=1 && H.prior(H.rcd[curr], H.rcd[curr/2])){
		SwapHeapElem(H, curr, curr/2);
		curr = curr/2;
	}
	return OK;
}

int RemoveFirstHeap(Heap &H, RcdType &e){
	//ɾ����H�ĶѶ����,����e���䷵��
	if(H.n <= 0)
		return ERROR;
	e = H.rcd[1];
	SwapHeapElem(H, 1, H.n);
	H.n--;
	if(H.n > 1)
		ShiftDown(H, 1);
	return OK;
}

int RemoveHeap(Heap &H, int pos, RcdType &e){
	//ɾ��λ��pos�Ľ��, ��e������ֵ
	if(pos<=0 || pos>H.n)
		return ERROR;
	e = H.rcd[pos];
	SwapHeapElem(H, pos, H.n);
	H.n--;
	if(H.n>1)
		ShiftDown(H, pos);
	return OK;
}

/*
void HeapSort(RcdSqList *L){
	//������
	Heap H;
	int i, e;
	MakeHeap(H, L.rcd, L.length, 1, greatPrior);
	for(i = H.n; i>0; i--)
		RemoveFirstHeap(H, e); 
}
*/

int main(){
	int E[7] = {0, 42, 58, 68, 98, 86, 42};
	Heap H;
	int e;
	InitHeap(H, 10);
	MakeHeap(H, E, 6, 1, greatPrior);
	for(int i=1;i<=H.n;i++)
		printf("H.rcd[%d]: %d\n",i,H.rcd[i]);
	printf("\n");
	InsertHeap(H, 59);
	for(int i=1;i<=H.n;i++)
		printf("H.rcd[%d]: %d\n",i,H.rcd[i]);
	printf("\n");
	RemoveFirstHeap(H, e);
	printf("e: %d\n", e);
	for(int i=1;i<=H.n;i++)
		printf("H.rcd[%d]: %d\n",i,H.rcd[i]);
	RemoveHeap(H, 3, e);
	printf("e: %d\n", e);
	for(int i=1;i<=H.n;i++)
		printf("H.rcd[%d]: %d\n",i,H.rcd[i]);
	HeapSort(E, 6);
	for(int i=1; i<7; i++)
		printf("%d\n",E[i]);
}
