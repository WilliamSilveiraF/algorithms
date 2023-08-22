package main
import (
	"fmt"
)

func main() {
	var distance int;
	fmt.Scanln(&distance);
	var fuel float64;
	fmt.Scanln(&fuel);

	fmt.Printf("%.3f km/l\n", float64(distance) / fuel);
}