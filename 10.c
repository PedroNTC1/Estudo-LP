#include <stdio.h>

// Função que conta o número de caracteres em uma string
int contar(const char *str) {
    int count = 0; // Inicializa o contador com 0
    while (*str != '\0') { // Itera até encontrar o caractere nulo ('\0')
        count++; // Incrementa o contador
        str++; // Avança para o próximo caractere
    }
    return count; 
}

int main() {
    char texto[] = "Exemplo"; // Declara uma string
    printf("Tamanho: %d\n", contar(texto)); // Imprime o tamanho da string
    return 0; }
