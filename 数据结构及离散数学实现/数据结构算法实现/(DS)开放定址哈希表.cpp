#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1

typedef int RcdType;
typedef int KeyType;
typedef struct{
	RcdType *rcd;
	int size;
	int count;
	int * tag;//标记，0：空；1：有效；-1：已删除 
	int (*hash)(KeyType key, int hashSize);
	void (*collision)(int &hashValue, int hashSize);//函数指针变量，用于处理冲突的函数 
} HashTable;

int hash(int key, int hashSize){
	return (3*key)%hashSize;
}

void collision(int &hashValue, int hashSize){//线性探测法处理冲突 
	hashValue = (hashValue+1)%hashSize;
}

int InitHash(HashTable &H, int size, int (*hash)(KeyType, int), void (*collision)(int &, int)){
	H.rcd = (RcdType*)malloc(size*sizeof(RcdType));
	int i;
	H.tag = (int *)malloc(size*sizeof(int));
	if(H.tag == NULL || H.rcd == NULL)
		return OVERFLOW;
	for(i=0; i<size; i++)
		H.tag[i] = 0;
	H.size = size;
	H.hash = hash;
	H.collision = collision;
	H.count = 0;
	return OK;
}

int SearchHash(HashTable H, int key, int &p, int &c){
	p = H.hash(key, H.size);
	while((H.rcd[p]!=key && H.tag[p]==1) || H.tag[p]==-1){
		H.collision(p, H.size);
		c++;
	}
	if(H.rcd[p] == key && H.tag[p] == 1)
		return OK;
	else
		return NULL;
}

int InsertHash(HashTable &H, int e){
	int c=0, j;
	if(SearchHash(H, e, j, c))
		return ERROR;
	H.rcd[j] = e;
	H.tag[j]= 1;
	H.count++;
	return c;
}

int DeleteHash(HashTable &H, KeyType key, RcdType &e){
	int c=0, j;
	if(!SearchHash(H, key, j, c))
		return ERROR;
	e = H.rcd[j];
	H.tag[j] = -1;
	H.count--;
	return OK;
}

void TraverseHash(HashTable H){
	for(int i=0; i<H.size; i++){
		printf("num: %d, rcd: %d, tag: %d\n", i, H.rcd[i], H.tag[i]);
	}
	printf("traverse done!\n");
}

int main(){
	HashTable H1;
	int p, c, e;
	InitHash(H1, 10, hash, collision);
	TraverseHash(H1);
	InsertHash(H1, 12);
	InsertHash(H1, 14);
	TraverseHash(H1);
	printf("search hash:%d\n", SearchHash(H1, 14, p, c));
	printf("delete hash:%d\n",DeleteHash(H1, 14, e));
	printf("e: %d\n", e);
	printf("search hash:%d\n", SearchHash(H1, 14, p, c));
}
