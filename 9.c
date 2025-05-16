#include <stdio.h>
#include <stdlib.h>

// Função que clona um vetor
int* clonar(int *vetor, int tamanho) {
    int *novo = (int *)malloc(tamanho * sizeof(int)); // Aloca memória para o novo vetor
    for (int i = 0; i < tamanho; i++) { // Copia os elementos do vetor original para o novo vetor
        novo[i] = vetor[i];
    }
    return novo; // Retorna o ponteiro para o novo vetor
}

int main() {
    int original[] = {1, 2, 3, 4, 5}; // Declara um vetor original
    int *copia = clonar(original, 5); // Clona o vetor original

    for (int i = 0; i < 5; i++) { // Imprime os elementos do vetor clonado
        printf("%d ", copia[i]);
    }

    free(copia); // Libera a memória alocada para o vetor clonado
    return 0; 
}
