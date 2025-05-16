#include <stdio.h>

int main() {
    int vetor[] = {1, 2, 3, 4, 5}; // Declara um vetor de inteiros com 5 elementos
    int *p = vetor; // Ponteiro 'p' aponta para o início do vetor
    for (int i = 0; i < 5; i++) { 
        printf("%d ", *(p + i)); // Acessa os elementos do vetor usando aritmética de ponteiros
    }
    return 0; 
}
