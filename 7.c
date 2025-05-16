#include <stdio.h>

int main() {
    int x = 10; // Declara uma variável inteira e inicializa com 10
    int *p = &x; // Ponteiro 'p' aponta para o endereço de 'x'
    int **pp = &p; // Ponteiro para ponteiro 'pp' aponta para o endereço de 'p'

    **pp = 30; // Altera o valor de 'x' indiretamente usando o ponteiro para ponteiro
    printf("Valor de x: %d\n", x); // Imprime o valor atualizado de 'x'
    return 0; // Indica que o programa terminou com sucesso
}
