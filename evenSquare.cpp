#include <stdio.h>
#include <iostream>
#include <iomanip>
using namespace std;

int square(int number) {
    return number * number;
}

int main() {
    
    int in00;
    std::cin >> in00;
    for (int i = 1; i < in00 + 1; i++) {
        if (i % 2 == 0) {
            cout << i << "^2 = " << square(i) << endl;
        };
    };

    return 0;
}