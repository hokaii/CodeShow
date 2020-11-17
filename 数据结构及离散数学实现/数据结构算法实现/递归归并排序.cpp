//二路归并 
void Merge(RcdType SR[], RcdType TR[], int i, int m, int n){
	//将相邻的有序区间SR[i.m]和SR[m+1,n]归并为有序的TR[i.n]
	int k,j;
	for(j=m+1, k=i; i<=m && j<=n; ++k){
		//将SR中记录按关键字从小到大地复制到TR中
		if(SR[i].key <= TR[j].key)
			TR[k] = SR[i++];
		else
			TR[k] = SR[j++]; 
	} 
	while(i<=m)
		TR[k++] = SR[i++];
	while(j<=n)
		TR[k++] = SR[j++]; 
} 

void MSort(RcdType R1[], RcdType R2[], int i, int s, int t){
	//对R1[s..t]归并排序,若i为奇数,则排序后的记录存入R2[s..t],否则存入R1[s..t]
	int m;
	if(s == t){
		if(1 == i%2)
			R2[s] = R1[s]; 
	} 
	else{
		m = (s+t)/2;
		MSort(R1, R2, i+1, s, m);
		MSort(R1, R2, i+1, m+1, t);
		if(1==i%2)
			Merge(R1,R2,s,m,t);
		else
			Merge(R2,R1,s,m,t); 
	}
}

void MergeSort(RcdSqlList &L) {
	RcdType *R;
	R = (RcdType*)malloc((L.length+1)*sizeof(RcdType));
	MSort(L.rcd,R,0,1,L.length);
	free(R);
}
