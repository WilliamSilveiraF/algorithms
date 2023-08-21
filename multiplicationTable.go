package main
import (
	"fmt"
)

func main() {
	var n int;
	fmt.Scanln(&n);

	for idx := 1; idx < 11; idx++ {
		fmt.Printf("%d x %d = %d\n", idx, n, idx * n);
	}
}