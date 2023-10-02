#include <stdio.h>

int add(int a, int b, int c, int d, int e, int f)
{
	return a+b+c+d+e+f+10;
}

int main(int argc, char** argv, char** envp)
{
	int s = 0;
	int a, b;
	a = 10;
	b = 20;
	s = add(a, 9, 8, 7, 6, b);
	printf("s = %d\n", s);
	return 0;
}
