#include <stdio.h>

int A[] = {-3, 10, -6, 1}; // Coeficientes do polinômio

// Função para calcular x elevado a n
int expoente(int x, int n) {
    int tmp = 1;
    for (int i = 0; i < n; i++) {
        tmp *= x;
    }
    return tmp;
}

// Função recursiva para calcular o valor do polinômio em x
int Polrec(int x, int n) {
    if (n == 0) return A[0];
    int soma = A[n] * expoente(x, n) + Polrec(x, n - 1);
    return soma;
}

int main() {
    int n = 3; // Grau do polinômio (tamanho do vetor A - 1)
    for (int i = 1; i < 7; i++) {
        printf("P(%d) = %d\n", i, Polrec(i, n)); // Corrigido: chama Polrec ao invés de P
    }
    return 0;
}