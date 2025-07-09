#include <stdio.h>
 int a[4] = {2,7,-1,6};
 int max0(int n){
    if (n==0) {
        return(a[0]); }
    if ( a[n] > a[0] ) {
        int tmp = a[0];
        a[0] = a[n];
        a[n] = tmp;
    }//end-if-an
 int m = max0(n-1);
 return(m);
}//end-max0
int main() {
    int n = 3; // Índice do último elemento do array
    int max_value = max0(n);
    printf("O maior valor é: %d\n", max_value);
    return 0;
}