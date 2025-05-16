#include <stdio.h>
#include <stdlib.h>

int main() {
    int **matriz = (int **)malloc(3 * sizeof(int *)); // Aloca memória para 3 ponteiros de linhas
    for (int i = 0; i < 3; i++) {
        matriz[i] = (int *)malloc(3 * sizeof(int)); // Aloca memória para 3 colunas em cada linha
    }

    int valor = 1; // Inicializa o valor a ser preenchido na matriz
    for (int i = 0; i < 3; i++) { // Preenche a matriz com valores sequenciais
        for (int j = 0; j < 3; j++) {
            matriz[i][j] = valor++;
        }
    }

    for (int i = 0; i < 3; i++) { // Imprime os valores da matriz
        for (int j = 0; j < 3; j++) {
            printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }

    for (int i = 0; i < 3; i++) { // Libera a memória alocada para cada linha
        free(matriz[i]);
    }
    free(matriz); // Libera a memória alocada para os ponteiros
    return 0; 
}
