#include <stdio.h>

int main() {
   int x = 10;
   int *p = &x;
   *p = 20;  // altera o valor de x via ponteiro
   printf("Valor de x: %d\n", x);
   return 0;
}