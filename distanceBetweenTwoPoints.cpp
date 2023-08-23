#include <stdio.h>
#include <iomanip>
#include <iostream>
#include <math.h>

int main() {
    float x1, y1, x2, y2;
    float diffDeXQuad, diffDeYQuad, res;
    
    std::cin >> x1 >> y1 >> x2 >> y2;

    diffDeXQuad = pow((x2 - x1), 2);
    diffDeYQuad = pow((y2 - y1), 2);

    res = sqrt(diffDeXQuad + diffDeYQuad);

    std::cout << std::fixed << std::setprecision(4) << res << std::endl;
    return 0;
};