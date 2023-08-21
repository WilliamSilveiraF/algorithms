#include <stdio.h>
#include <iostream>
#include <iomanip>

int main() {
    int distance;
    float fuel;

    std::cin >> distance >> fuel;
    std::cout << std::fixed << std::setprecision(3) << distance / fuel << " km/l" << std::endl;
    return 0;
};