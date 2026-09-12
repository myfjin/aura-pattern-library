package main
import ("fmt"; "os")
// clamp into [lo,hi]
func clamp(x, lo, hi int) int { if x<lo {return lo}; if x>hi {return hi}; return x }
func main() {
	if clamp(5,0,10)!=5 || clamp(-3,0,10)!=0 || clamp(99,0,10)!=10 {
		fmt.Fprintln(os.Stderr, "clamp wrong"); os.Exit(1)
	}
	fmt.Println("clamp passed")
}
