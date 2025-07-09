#include <stdio.h>

// Função que retorna a soma de dois inteiros
int soma(int a, int b) {
    return a + b;
}

// Função que retorna o produto de dois inteiros
int multiplica(int a, int b) {
    return a * b;
}

// Função que recebe outra função como parâmetro e executa a operação
void opera(int x, int y, int (*func)(int, int)) {
    printf("Resultado: %d\n", func(x, y)); // Chama a função passada como parâmetro
}

int main() {
    opera(3, 4, soma); // Chama a função 'opera' com a função 'soma'
    opera(3, 4, multiplica); // Chama a função 'opera' com a função 'multiplica'
    return 0; 
}