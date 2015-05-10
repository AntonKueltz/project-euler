#include <chrono>
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
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e006() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
