#include <stdio.h>

#define N 1000000000

int main(void) {
    double x, final;
    int i;

    final = 1;
    x = 1 + 1.0 / N;

    for (i = 0; i < N; i++) {
        final = final * x;
    }

    printf("Resultado=%lf\n", final);
    return 0;
}