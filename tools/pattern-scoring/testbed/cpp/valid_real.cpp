#include <cassert>
#include <iostream>
// Clamp x into [lo,hi]. Total function.
long clamp(long x, long lo, long hi){ return x<lo?lo:(x>hi?hi:x); }
int main(){
    assert(clamp(5,0,10)==5);
    assert(clamp(-3,0,10)==0);
    assert(clamp(99,0,10)==10);
    std::cout << "clamp PASS" << std::endl; return 0;
}
