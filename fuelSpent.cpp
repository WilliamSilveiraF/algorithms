#include <stdio.h>
#include <iostream>
#include <iomanip>

int main() {
    int timing, speedAvarage;
    double fuelNedded;

    std::cin >> timing;
    std::cin >> speedAvarage;
    fuelNedded = static_cast<double>(timing * speedAvarage) / 12;
    std::cout << std::fixed << std::setprecision(3) << fuelNedded << std::endl;


    return 0;

};