package main
import (
	"fmt"
	"math"
)

func square(number float64) float64 {
	return number * number;
}

func main() {
	var x1, x2, y1, y2 float64;
	var diffDeXQuad, diffDeYQuad, res float64;

	fmt.Scanln(&x1, &y1);
	fmt.Scanln(&x2, &y2);

	diffDeXQuad = square(x2 - x1);
	diffDeYQuad = square(y2 - y1);

	res = math.Sqrt(diffDeXQuad + diffDeYQuad);

	fmt.Printf("%.4f\n", res)
}
