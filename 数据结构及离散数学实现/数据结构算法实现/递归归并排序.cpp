//��·�鲢 
void Merge(RcdType SR[], RcdType TR[], int i, int m, int n){
	//�����ڵ���������SR[i.m]��SR[m+1,n]�鲢Ϊ�����TR[i.n]
	int k,j;
	for(j=m+1, k=i; i<=m && j<=n; ++k){
		//��SR�м�¼���ؼ��ִ�С����ظ��Ƶ�TR��
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
	//��R1[s..t]�鲢����,��iΪ����,�������ļ�¼����R2[s..t],�������R1[s..t]
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
