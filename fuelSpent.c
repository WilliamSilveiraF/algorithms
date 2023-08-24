#include <stdio.h>


int main() {
    int timing, speedAvarage;
    double fuelNedded;
    scanf("%d", &timing);
    scanf("%d", &speedAvarage);
    
    fuelNedded = (double)(timing * speedAvarage) / 12;

    printf("%.3lf\n", fuelNedded);

    return 0;
};