#include <stdio.h>
#include <iostream>
#include <iomanip>

int main() {
    float gradeA, gradeB, gradeC, avarage;

    std::cin >> gradeA >> gradeB >> gradeC;
    avarage = (gradeA * 2.0 + gradeB * 3.0 + gradeC * 5.0) / 10.0;

    std::cout << "MEDIA = " << std::fixed << std::setprecision(1) << avarage << std::endl;
    return 0;
};