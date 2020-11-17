#include <stdio.h>

void hanoi(int n, char x, char y, char z){
	void move(int i, char x, char y);
	if(n == 1)
		move(1, x, z);
	else{
		hanoi(n-1, x, z, y);
		move(n, x, z);
		hanoi(n-1, y, x, z);
	}
}

void move(int i, char x, char y){
	printf("将第 %d 个圆盘从 %c 柱子移到 %c 柱子\n", i, x, y);
}

int main(){
	char x = 'x';
	char y = 'y';
	char z = 'z';
	hanoi(4, x, y, z);
}
