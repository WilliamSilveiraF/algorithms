#include <stdio.h>

int main() {
    float gradeA, gradeB, gradeC, avarage;
    scanf("%f", &gradeA);
    scanf("%f", &gradeB);
    scanf("%f", &gradeC);
    
    avarage = (gradeA * 2.0 + gradeB * 3.0 + gradeC * 5.0) / 10.0;

    printf("MEDIA = %.1f\n", avarage);
    return 0;
};