#include "(DS)Á´Õ».cpp"

int main(){
	LStack S;
	int t;
	InitStack_LS(S);
	Push_LS(S, 12);
	Push_LS(S, 22);
	Push_LS(S, 23);
	Push_LS(S, 54);
	Pop_LS(S, t);
	printf("t is: %d\n", t);
	GetTop_LS(S, t);
	printf("t is: %d\n", t);
	printf("%d\n",StackEmpty_LS(S));
	Traverse_LS(S);
}
