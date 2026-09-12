#include <cassert>
long add(long a,long b){ return a+b   // missing semicolon+brace
int main(){ assert(add(2,2)==4); return 0; }
