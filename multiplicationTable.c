#include <stdio.h>

int main() {
    int n;
    
    scanf("%d", &n);

    for (int idx = 1; idx < 11; idx++) {
        printf("%d x %d = %d\n", idx, n, idx * n);
    };
    return 0;
};