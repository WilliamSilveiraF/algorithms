package main
import (
	"fmt"
)

func square(number int) int {
	return number * number;
}

func main() {
	var n int;

	fmt.Scanln(&n);

	for i := 1; i < n + 1; i++ {
		if (i % 2 == 0) {
			fmt.Printf("%d^2 = %d\n", i, square(i));
		};
	};
};