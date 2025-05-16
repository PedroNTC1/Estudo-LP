#include <stdio.h>

// Função para trocar os valores de dois inteiros usando ponteiros
void trocar(int *a, int *b) {
    int temp = *a; // Armazena o valor apontado por a em uma variável temporária
    *a = *b;       // Atribui o valor apontado por b ao endereço apontado por a
    *b = temp;     // Atribui o valor armazenado em temp ao endereço apontado por b
}

int main() {
    int x = 5, y = 10; // Declara duas variáveis inteiras e inicializa com valores
    trocar(&x, &y);    // Chama a função trocar passando os endereços de x e y
    printf("x = %d, y = %d\n", x, y); // Imprime os valores de x e y após a troca
    return 0; 
}