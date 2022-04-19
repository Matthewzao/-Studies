#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main() {

	float a,b,c,delta,x1,x2;
	
	printf("calculando raizes de uma funcao do 2 grau \n");
	printf("digite um valor do coeficiente a:  ");
	scanf("%f", &a);
	printf("digite um valor do coeficiente b:  ");
	scanf("%f", &b);
	printf("digite um valor do coeficiente c:  ");
	scanf("%d",&c);
	
	delta=(b*b-4*a*c);
	printf("\n");
	printf("o valor de delta e %.2f\n\n",delta);
	
	if (delta>=0) {
		x1=((-b+sqrt(delta))/2*a);
		x2=((-b-sqrt(delta))/2*a);
		printf("x1= %.2f\n",x1);
		printf("x2= %.2f\n",x2);
	}
	
	
	}
	