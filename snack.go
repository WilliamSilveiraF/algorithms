package main
import (
	"fmt"
)

func main() {
	var a int;
	var b, price float64;

	fmt.Scanln(&a, &b);

	switch a {
		case 1:
			price = 4.00;
		case 2:
			price = 4.50;
		case 3:
			price = 5.00;
		case 4:
			price = 2.00;
		case 5:
			price = 1.50;
	}

	fmt.Printf("Total: R$ %.2f\n", price * b);
}