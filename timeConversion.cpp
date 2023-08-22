#include <stdio.h>
#include <iostream>
#include <iomanip>

int main() {
    int time;
    std::cin >> time;

    int hours = time / 3600;
    time = time - (hours * 3600);
    int minutes = time / 60;
    time = time - (minutes * 60);
    int seconds = time;

    std::cout << hours << ":" << minutes << ":" << seconds << std::endl;

    return 0;
};