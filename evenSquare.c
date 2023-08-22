#include <stdio.h>

int square(int number) {
    return number * number;
};

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 1; i < n + 1; i++) {
        if (i % 2 == 0) {
            printf("%d^2 = %d\n", i, square(i));
        };
    };
    return 0;
};