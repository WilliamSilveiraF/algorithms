#include <stdio.h>
#include <iostream>
#include <iomanip>

int main() {
    int donaMonica, filhoA, filhoB, filhoC;
    filhoC = donaMonica - (filhoA + filhoB);

    std::cin >> donaMonica;
    std::cin >> filhoA;
    std::cin >> filhoB;

    filhoC = donaMonica - (filhoA + filhoB);

    int oldest = std::max({ filhoA, filhoB, filhoC });

    std::cout << oldest << std::endl;

    return 0;
};