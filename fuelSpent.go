package main
import (
	"fmt"
)

func main() {
	var timing, speedAvarage int;
	var fuelNedded float64;


	fmt.Scanln(&timing);
	fmt.Scanln(&speedAvarage);
	fuelNedded = float64(timing * speedAvarage) / 12.0;

	fmt.Printf("%.3f\n", fuelNedded);
}