#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1
#define MAXSIZE 100

typedef int KeyType;
typedef struct{
	RcdType * rcd;
	int length;
	int size;
} RcdSqList;
typedef struct {
	KeyType key;
} RecordType, RcdType;


void InsertSort(RcdSqList &L) {
	int i, j;
	for(i=1; i<L.length; i++)
		if(L.rcd[i].key < L.rcd[i+1].key){
			L.rcd[0] = L.rcd[i+1];
			j = i+1;
			do{
				j--;L.rcd[j+1] = L.rcd[j];
			}
			while(L.rcd[j-1].key > L.rcd[0].key);
			L.rcd[0] = L.rcd[i];
		}
}

int main(){
	RcdSqList L;
	L.rcd = ()
}
