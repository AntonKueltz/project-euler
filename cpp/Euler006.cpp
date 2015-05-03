#include <cstdint>
#include <iostream>

uint64_t e006(){
    uint64_t sumSquare = 0, squareSum = 0;
    uint64_t n = 100;

    sumSquare = (50 * 101) * (50 * 101);
    for(uint64_t i = 1; i <= n; ++i) squareSum += i * i;

    return sumSquare - squareSum;
}

int main(int argc, char * argv[]){
    std::cout << e006() << std::endl;
}
