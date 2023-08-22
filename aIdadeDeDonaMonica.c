#include <stdio.h>

int max_of_three(int a, int b, int c) {
    int max = a;
    
    if (b > max) {
        max = b;
    }
    if (c > max) {
        max = c;
    }
    
    return max;
}


int main() {
    int donaMonica, filhoA, filhoB, filhoC, maxAge;
    
    scanf("%d", &donaMonica);
    scanf("%d", &filhoA);
    scanf("%d", &filhoB);

    filhoC = donaMonica - (filhoA + filhoB);

    int oldest = max_of_three(filhoA, filhoB, filhoC);

    printf("%d\n", oldest);

    return 0;
};