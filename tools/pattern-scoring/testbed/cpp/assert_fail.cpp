#include <cassert>
#include <iostream>
long add(long a,long b){ return a+b; }
int main(){
    assert(add(2,2)==5);  // WILL fail
    std::cout << "add PASS" << std::endl; return 0;
}
