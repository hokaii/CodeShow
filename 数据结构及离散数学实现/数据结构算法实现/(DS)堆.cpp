#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1

typedef int RcdType;
typedef int KeyType;
typedef struct{
	RcdType *rcd;//堆基址,0号单元闲置 
	int n;//堆长度 
	int size;//堆容量 
	int tag; //小顶堆和大顶堆的标志, tag=0为小顶堆,tag=1为大顶堆 
	int (*prior)(KeyType, KeyType); //函数变量,用于关键字优先比较 
} Heap; //堆类型 

int greatPrior(int x, int y){
	//大顶堆优先函数 
	return x>=y;
} 

int lessPrior(int x, int y){
	//小顶堆优先函数 
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
	//用E建长度为n的堆H, 容量为size, 当tag为0或1时分别表示小顶堆和大顶堆 
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
	//销毁堆H 
	for(int i=H.n; i>=0; i--){
		free(&(H.rcd[i]));
	}
	free(&H);
	return OK;
}

int SwapHeapElem(Heap &H, int i, int j){
	//交换堆H中的第i个结点和第j个结点
	RcdType t;
	if(i<=0 || j<=0 || i>H.n || j>H.n)
		return ERROR;
	t = H.rcd[i];
	H.rcd[i] = H.rcd[j];
	H.rcd[j] = t;
	return OK;
} 

void ShiftDown(Heap &H, int pos){//※ 
	//对堆H中位置为pos的结点做筛选,将以pos为根的子树调整为子堆
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
	//将e插入堆 
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
	//删除堆H的堆顶结点,并用e将其返回
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
	//删除位置pos的结点, 用e返回其值
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
	//堆排序
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
