#include <stdio.h>
#include <stdlib.h>
# define MaxSize 100

typedef struct BiTNode{
	int weight;
	struct BiTNode *left, *right;
}BiTNode, *BiTree;

int GetWPL(BiTree T){
	if(!T)
		return 0;
	int front=-1, rear=-1;
	int last=0, level=0, wpl=0;
	BiTree Q[MaxSize];
	Q[++rear] = T;
	BiTree p;
	while(front < rear){
		p = Q[++front];
		if(p->left)
			Q[++rear] = p->left;
		if(p->right)
			Q[++rear] = p->right;
		if(front == last){
			level++;
			last = rear;
		}
		if((!p->left)&&(!p->right)){
			printf("\n%d, %d, %d\n", p->weight, wpl, level);
			wpl += (level*p->weight);
		}
			
	}
	return wpl-p->weight;
}

int WPL_PreOrder(BiTree root, int deep){
	static int wpl=0;
	if(root->left==NULL && root->right==NULL)
		wpl+= deep*root->weight;
	if(root->left!=NULL)
		WPL_PreOrder(root->left, deep+1);
	if(root->right!=NULL)
		WPL_PreOrder(root->right, deep+1);
	return wpl;	
}

int WPL(BiTree root){
	return WPL_PreOrder(root, 0);
}



BiTree CreateTree(){
	BiTree Tree[10];
	BiTree t;
	for(int i=0; i<10; i++){
		t = (BiTree)malloc(sizeof(BiTNode));
		Tree[i] = t;
		Tree[i]->weight=i;
	}
	BiTree p=Tree[0];
	Tree[1]->left=Tree[3];
	Tree[1]->right=Tree[4];
	Tree[3]->left=NULL;
	Tree[3]->right=NULL;
	Tree[4]->right=NULL;
	Tree[2]->left=Tree[5];
	Tree[2]->right=Tree[6];
	Tree[4]->left=Tree[7];
	Tree[7]->right=NULL;
	Tree[7]->left=NULL;
	Tree[5]->right=NULL;
	Tree[5]->left=NULL;
	Tree[6]->right=Tree[8];
	Tree[6]->left=NULL;
	Tree[8]->right=NULL;
	Tree[8]->left=NULL;
	p->left=Tree[1];
	p->right=Tree[2];
	return p;
}

void PreOrder(BiTree T){
	if(T){
		printf("%d\n",T->weight);
		PreOrder(T->left);
		PreOrder(T->right);
	}
}

int main(){
	BiTree T = CreateTree();
	PreOrder(T);
	printf("\n%d\n", GetWPL(T));
	printf("(");
	printf("\n%d\n", WPL(T));
}
