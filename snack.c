#include <stdio.h>

int main() {
    int a;
    float b, price;

    scanf("%d %f", &a, &b);

    switch(a) {
        case 1:
            price = 4.00;
            break;
        case 2:
            price = 4.50;
            break;
        case 3:
            price = 5.00;
            break;
        case 4:
            price = 2.00;
            break;
        case 5:
            price = 1.50;
            break;
        default:
            return 1;
    }

    printf("Total: R$ %.2f\n", price * b);
    return 0;
}