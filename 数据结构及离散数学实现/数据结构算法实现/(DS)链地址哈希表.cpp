#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1

typedef int RcdType;
typedef struct Node{
	RcdType r;
	struct Node *next;
} Node;
typedef int KeyType;
typedef struct{
	Node **rcd;
	int size;
	int count;
	int (*hash)(KeyType key, int hashSize);
} HashTable;

int InitHash(HashTable &H, int size, int (*hash)(KeyType, int)){
	int i;
	H.rcd = (Node**)malloc(size*sizeof(Node*));
	if(NULL == H.rcd)
		return OVERFLOW;
	for(i=0; i<size; i++)
		H.rcd[i] = NULL;
	H.size = size;
	H.hash = hash;
	H.count = 0;
	return OK;
}

int hash(int key, int hashSize){
	return (3*key)%hashSize;
}

Node* SearchHash(HashTable &H, KeyType key){
	int p = H.hash(key, H.size);
	Node *np;
	for(np=H.rcd[p]; np!=NULL; np=np->next)
		if(np->r == key)
			return np;
	return NULL;
}

int InsertHash(HashTable &H, RcdType e){
	int p;
	Node *np;
	if(SearchHash(H, e) == NULL){
		p = H.hash(e, H.size);
		np = (Node*)malloc(sizeof(Node));
		np->r = e;
		np->next = H.rcd[p];
		H.rcd[p] = np;
		H.count++;
		return OK;
	}
	else
		return ERROR;
}

int DeleteHash(HashTable &H, int key){
	int i = H.hash(key, H.size);
	Node *p = H.rcd[i];
	while(p!=NULL){
		if(p->r == key){
			H.rcd[i] = p->next;
			free(p);
			return OK;
		}
		p = p->next;
	}
	return NULL;
}

int main(){
	HashTable H1;
	InitHash(H1, 10, hash);
	for(int i=0; i<10; i++)
		printf("hashtable[%d]: %d\n", i, H1.rcd[i]);
	printf("search elem %d\n",SearchHash(H1, 2));
	InsertHash(H1, 2);
	InsertHash(H1, 4);
	InsertHash(H1, 6);
	InsertHash(H1, 5);
	printf("search elem %d\n",SearchHash(H1, 2));
	printf("search elem %d\n",SearchHash(H1, 5));
//	for(int i=0; i<10; i++)
//		printf("hashtable[%d]: %d\n", i, H1.rcd[i]);
	DeleteHash(H1, 2);
	for(int i=0; i<10; i++)
		printf("hashtable[%d]: %d\n", i, H1.rcd[i]);
}
