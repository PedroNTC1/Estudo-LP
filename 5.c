#include <stdio.h>

int main() {
    int vetor[] = {1, 2, 3, 4, 5}; // Declara um vetor de inteiros com 5 elementos
    int soma = 0; // Inicializa a variável soma com 0
    int *p = vetor; // Ponteiro 'p' aponta para o início do vetor

    for (int i = 0; i < 5; i++) { // Itera sobre os elementos do vetor
        soma += *(p + i); // Soma os valores do vetor usando aritmética de ponteiros
    }

    printf("Soma: %d\n", soma); // Imprime a soma dos elementos do vetor
    return 0; // Indica que o programa terminou com sucesso
}