package main
import (
	"fmt"
)

func main() {
	var donaMonica int;
	var filhoA int;
	var filhoB int;

	fmt.Scanln(&donaMonica);
	fmt.Scanln(&filhoA);
	fmt.Scanln(&filhoB);

	filhoC := donaMonica - (filhoA + filhoB);

	oldest := max(filhoA, filhoB, filhoC);

	fmt.Printf("%d\n", oldest);
}

func max(nums ...int) int {
	var maxVal int = nums[0]
	for _, num := range nums {
		if num > maxVal {
			maxVal = num;
		}
	}
	return maxVal
}