#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1
#define UNVISITED 0
#deifne VISITED 1
#define INFINITY MAXINT//�����������������ֵ 

typedef enum{
	DG, DN, UDG, UDN//ͼ��4�����ͣ�����ͼ�������Ȩͼ������ͼ�������Ȩͼ 
} GraphKind; 

typedef struct{
	VexType *vexs;//�������� 
	int **arcs;//��ϵ����, ����Ȩͼ, ��0��1��ʾ���ڷ�
			   //�Դ�Ȩͼ, ��ΪȨֵ��INFINITY 
	int n, e;//�������ͱ��� 
	GraphKind kind;//ͼ������ 
	int *tags;//��־����, ��������ͼ�ı����б�Ƕ��������� 
} MGraph;//�ڽ�����

typedef struct{
	VexType v, w;//��(��)�Ķ˵� 
	int info;//�Դ�Ȩͼ, ΪȨֵ 
} ArcInfo; //��(��)��Ϣ
 
int LocateVex_M(MGraph G, VexType v){
	//���Ҷ���v��ͼG�е�λ��
	int i;
	for(i=0; i<G.n; i++)
		if(v == G.vexs[i])
			return i;
	return -1; 
} 

int CreateGraph_M(MGraph &G, GraphKind kind, VexType *vexs, int n, ArcInfo *arcs, int e){
	//������n�������e���ߵ�kind���ͼG,vexsΪ������Ϣ, arcsΪ����Ϣ
	if(n<0 || e<0 || (n>0 && !vexs) || (e>0 && !arcs))
		return ERROR;
	G.kind = kind;
	switch(G.kind){
		case UDG:return CreateUDG_M(G, vexs, n, arcs, e);//��������ͼ 
		case DG: return CreateDG_M(G, vexs, n, arcs, e);//��������ͼ 
		case UDN:return CreateUDN_M(G, vexs, n, arcs, e);//���������Ȩͼ 
		case DN: return CreateDN_M(G, vexs, n, arcs, e);//���������Ȩͼ 
		default: return ERROR;
	} 
} 

int InitGraph_M(MGraph &G, GraphKind kind, VexType *vexs, int n){
	//��ʼ����n���������ޱߵ�kind���ͼG
	int i, j, info;
	if(n<0 || (n>0 && !vexs))
		return ERROR;
	if(kind == DG || kind == UDG)
		info = 0;
	else if(kind == DN || kind == UDN)
		info = INFINITY;
	else
		return ERROR;
	G.n = n;
	G.e = 0;
	G.kind = kind;
	if(0 == n)
		return OK;
	if(NULL == (G.vexs = (VexType*)malloc(n*sizeof(VexType))))
		return OVERFLOW;
	for(i=0; i<n; i++)
		G.vexs[i] = vexs[i];
	if(NULL == (G.arcs = (int **)malloc(n*sizeof(int *))))
		return OVERFLOW;
	for(i=0; i<n; i++)
		if(NULL == (G.arcs[i] = (int *)malloc(n * sizeof(int))))
			return OVERFLOW;
	if(NULL == (G.tags = (int *)malloc(n*sizeof(int))))
		return OVERFLOW; 
	for(i=0; i<n; i++){
		G.tags[i] = UNVISITED;
		for(j=0; j<n; j++)
			G.arcs[i][j] = info;
	}
	return OK;
} 

int CreateUDG_M(MGraph &G, VexType *vexs, int n, ArcInfo *arcs, int e){
	//������n�������e���ߵ�����ͼG,vexsΪ������Ϣ,arcsΪ����Ϣ
	int i, j, k;
	VexType v, w;
	if(InitGraph_M(G, G.kind, vexs, n)!=OK)
		return ERROR;
	G.e = e;
	for(i=0; i<G.e; i++){
		v = arcs[i].v;
		w = arcs[i].w;
		j = LocateVex_M(G, v);
		k = LocateVex_M(G, w);
		if(j<0 || k<0)
			return ERROR;
		G.arcs[j][k] = G.arcs[j][i] = 1;
	}
	return OK;
}

int FirstAdjVex_M(MGraph G, int k){
	//��ͼG��k����ĵ�һ���ڽӶ����λ��
	int i;
	if(k<0 || k>G.) 
}
