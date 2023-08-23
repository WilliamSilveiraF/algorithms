#include <stdio.h>
#include <math.h>

int main() {
    float x1, y1, x2, y2;
    float diffDeXQuad, diffDeYQuad, res;

    scanf("%f %f", &x1, &y1);
    scanf("%f %f", &x2, &y2);

    diffDeXQuad = pow((x2 - x1), 2);
    diffDeYQuad = pow((y2 - y1), 2);

    res = sqrt(diffDeXQuad + diffDeYQuad);

    printf("%.4f\n", res);
}
