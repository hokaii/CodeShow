void search(int n,int num[],char name[N][8])                 //折半查找法的函数
{
	int top,bott,mid,loca,sign;
	top=0;
	bott=9;
	loca=0；
	sign=1;
	if((n<num[0])||(n>num[N-1]))
	loca=-1;
	while((sign==1)&&(top<=bott))
	{
		mid=(bott+top)/2;
		if(n==num[mid])
		{
			loca=mid;
			printf("NO. %d ,his name is %s. \n",n,name[loca]);
			sign=-1;
		}
		else if(n<num[mid])
		bott=mid-1;
		else
		top=mid+1;
	 } 
	 if(sign==1||loca==-1)
	   printf("%d not been found.\n",n);
 } 
