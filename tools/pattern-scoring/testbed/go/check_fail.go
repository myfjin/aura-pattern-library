package main
import ("fmt"; "os")
func add(a,b int) int { return a+b }
// self-test is wrong: 2+2 != 5, so it must os.Exit(1)
func main() {
	if add(2,2)!=5 { fmt.Fprintln(os.Stderr,"add wrong"); os.Exit(1) }
	fmt.Println("add passed")
}
