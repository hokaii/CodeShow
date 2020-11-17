#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1

typedef struct{
	float coef;//系数 
	int expn;//指数 
}ElemType,Term;
typedef struct{
	Term *elem;
	int length;
}Poly;

int CreatePoly(Poly &P, Term e[], int n){
	int i;
	P.elem = (Term*)malloc(sizeof(Term)*n);
	if(NULL == P.elem)
		return OVERFLOW;
	for(i=0;i<n;i++)
		P.elem[i] = e[i];
	P.length = n;
	return OK;
}

int PrintPoly(Poly P){
	for(int i=0;i<P.length;i++)
		printf("%f, %d\n",P.elem[i].coef,P.elem[i].expn);
}

int PolyLength(Poly P){
	return P.length;
}

void AddPoly(Poly pa, Poly pb, Poly &pc){
	int i=0,j=0,k=0;
	float c;
	pc.elem = (Term*)malloc((pa.length+pb.length)*sizeof(Term));
	//pc.length = pa.length + pb.length;
	if(NULL == pc.elem)
		printf("1 OVERFLOW");
	while(i<pa.length && j<pb.length){
		if(pa.elem[i].expn < pb.elem[j].expn){
			pc.elem[k] = pa.elem[i];
			i++;
			k++;
		}
		else if(pa.elem[i].expn == pb.elem[j].expn){
			c = pa.elem[i].coef + pb.elem[j].coef;
			if(c!=0){
				pc.elem[k].expn = pa.elem[i].expn;
				pc.elem[k].coef = c;
				k++;
			}
			i++;
			j++;
		}
		else{
			pc.elem[k] = pb.elem[j];
			j++;
			k++;
		}
	}
	for(i;i<pa.length;i++){
		pc.elem[k] = pa.elem[i];
		k++;
	}
	for(j;j<pb.length;j++){
		pc.elem[k] = pb.elem[j];
		k++;
	}
	if(k<pa.length+pb.length){
		if(NULL == (pc.elem = (Term*)realloc(pc.elem, k*sizeof(Term))))
			printf("2 OVERFLOW");
	}
	pc.length = k;
}

void SubPoly(Poly pa, Poly pb, Poly &pc){
	int i=0,j=0,k=0;
	float c;
	pc.elem = (Term*)malloc((pa.length+pb.length)*sizeof(Term));
	if(NULL == pc.elem)
		printf("3 OVERFLOW");
	while(i<pa.length && j<pb.length){
		if(pa.elem[i].expn < pb.elem[j].expn){
			pc.elem[k] = pa.elem[i];
			i++;
			k++;
		}
		else if(pa.elem[i].expn == pb.elem[j].expn){
			c = pa.elem[i].coef - pb.elem[j].coef;
			if(c!=0){
				pc.elem[k].coef = c;
				pc.elem[k].expn = pa.elem[i].expn;
				k++;
			}
			i++;
			j++;
		}
		else{
			pc.elem[k].coef = -pb.elem[j].coef; 
			pc.elem[k].expn = pb.elem[j].expn;
			k++;
			j++;
		}
	}
	for(i;i<pa.length;i++){
		pc.elem[k] = pa.elem[i];
		k++;
	}
	for(j;j<pb.length;j++){
		pc.elem[k].coef = -(pb.elem[j].coef);
		pc.elem[k].expn = pb.elem[j].expn;
		k++;
	}
	if(k < pa.length+pb.length){
		if(NULL == (pc.elem = (Term*)realloc(pc.elem, k*sizeof(Term))))
			printf("4 OVERFLOW");
	}
	pc.length = k;
}

/*TODO:void MulPoly(Poly pa, Poly pb, Poly &pc){
	int i=0,j=0,k=0;
	float c;
	pc.elem = (Term*)malloc((pa.length+pb.length)*sizeof(Term));
	while(i<pa.length && j<pb.length){
		
	}
}
*/

/*TODO: void DivPoly(Poly pa, Poly pb, Poly &pc){
}
*/

int main(){
	Term e[4];
	Term f[3];
	e[0].coef = -7.0;
	e[0].expn = 4;
	e[1].coef = 3.0;
	e[1].expn = 6;
	e[2].coef = 9.0;
	e[2].expn = 7;
	e[3].coef = 2.0;
	e[3].expn = 9;
	f[0].coef = 2.0;
	f[0].expn = 1;
	f[1].coef = 7.0;
	f[1].expn = 4;
	f[2].coef = -2.0;
	f[2].expn = 6;
	Poly pa,pb,pc;
	CreatePoly(pa, e, 4);
	CreatePoly(pb, f, 3);
	SubPoly(pa, pb, pc);
	PrintPoly(pc);
}
