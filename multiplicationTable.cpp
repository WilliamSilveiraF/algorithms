#include <stdio.h>
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    std::cin >> n;
    for (int idx = 1; idx < 11; idx++) {
        cout << idx << " x " << n << " = " << idx * n << endl;
    };
    return 0;
};