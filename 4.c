#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    printf("Digite o tamanho do vetor: "); // Solicita o tamanho do vetor ao usuário
    scanf("%d", &n); // Lê o tamanho do vetor

    int *vetor = (int *)malloc(n * sizeof(int)); // Aloca dinamicamente memória para o vetor
    if (vetor == NULL) return 1; // Verifica se a alocação foi bem-sucedida

    for (int i = 0; i < n; i++) { // Preenche o vetor com valores de 1 a n
        vetor[i] = i + 1;
    }

    for (int i = 0; i < n; i++) { // Imprime os elementos do vetor
        printf("%d ", vetor[i]);
    }

    free(vetor); // Libera a memória alocada dinamicamente
    return 0; 
}