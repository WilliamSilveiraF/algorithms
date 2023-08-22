package main
import ( 
	"fmt" 
)

func main() {
	var time int;
	fmt.Scanln(&time);

	hours := time / 3600;
	time = time - (hours * 3600);
	minutes := time / 60;
	time = time - (minutes * 60);
	seconds := time;

	fmt.Printf("%d:%d:%d\n", hours, minutes, seconds)
}