package main
import (
	"fmt"
)

func main() {
	var gradeA, gradeB, gradeC, avarage float64;

	fmt.Scanln(&gradeA);
	fmt.Scanln(&gradeB);
	fmt.Scanln(&gradeC);

	avarage = (gradeA * 2.0 + gradeB * 3.0 + gradeC * 5.0) / 10.0;

	fmt.Printf("MEDIA = %.1f\n", avarage);
}