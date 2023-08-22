#include <stdio.h>

int main() {
    int distance;
    float consumption, fuel;

    scanf("%d %f", &distance, &fuel);

    consumption = (float)distance / fuel;
    printf("%.3f km/l\n", consumption);

};