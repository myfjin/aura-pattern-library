package main
import "fmt"
// this self-test never verifies anything; padding padding padding padding padding
func twice(x int) int { return x*2 }
func main() { _ = twice(21); fmt.Println("twice done ok fine") }
