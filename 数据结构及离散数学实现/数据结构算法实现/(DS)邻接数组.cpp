#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1
#define UNVISITED 0
#deifne VISITED 1
#define INFINITY MAXINT//计算机允许的最大整数值 

typedef enum{
	DG, DN, UDG, UDN//图的4种类型，有向图、有向带权图、无向图和无向带权图 
} GraphKind; 

typedef struct{
	VexType *vexs;//顶点数组 
	int **arcs;//关系数组, 对无权图, 用0和1表示相邻否
			   //对带权图, 则为权值或INFINITY 
	int n, e;//顶点数和边数 
	GraphKind kind;//图的类型 
	int *tags;//标志数组, 可用于在图的遍历中标记顶点访问与否 
} MGraph;//邻接数组

typedef struct{
	VexType v, w;//边(弧)的端点 
	int info;//对带权图, 为权值 
} ArcInfo; //边(弧)信息
 
int LocateVex_M(MGraph G, VexType v){
	//查找顶点v在图G中的位序
	int i;
	for(i=0; i<G.n; i++)
		if(v == G.vexs[i])
			return i;
	return -1; 
} 

int CreateGraph_M(MGraph &G, GraphKind kind, VexType *vexs, int n, ArcInfo *arcs, int e){
	//创建含n个顶点和e条边的kind类的图G,vexs为顶点信息, arcs为边信息
	if(n<0 || e<0 || (n>0 && !vexs) || (e>0 && !arcs))
		return ERROR;
	G.kind = kind;
	switch(G.kind){
		case UDG:return CreateUDG_M(G, vexs, n, arcs, e);//创建无向图 
		case DG: return CreateDG_M(G, vexs, n, arcs, e);//创建有向图 
		case UDN:return CreateUDN_M(G, vexs, n, arcs, e);//创建无向带权图 
		case DN: return CreateDN_M(G, vexs, n, arcs, e);//创建有向带权图 
		default: return ERROR;
	} 
} 

int InitGraph_M(MGraph &G, GraphKind kind, VexType *vexs, int n){
	//初始化含n个顶点且无边的kind类的图G
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
	//创建含n个顶点和e条边的无向图G,vexs为顶点信息,arcs为边信息
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
	//求图G中k顶点的第一个邻接顶点的位序
	int i;
	if(k<0 || k>G.) 
}
