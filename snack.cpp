#include <stdio.h>
#include <iostream>
#include <iomanip>

int main() {
 
    int a;
    float b, price;

    std::cin >> a >> b;

    if (a == 1) {
        price = 4.00;
    } else if (a == 2) {
        price = 4.50;
    } else if (a == 3) {
        price = 5.00;
    } else if (a == 4) {
        price = 2.00;
    } else if (a == 5) {
        price = 1.50;
    }   

    std::cout << "Total: R$ " << std::fixed << std::setprecision(2) << price * b << std::endl;
 
    return 0;
}
