#include <chrono>
#include <cstdint>
#include <iostream>
#include <vector>

#include "EulerUtil.hpp"

uint64_t e010(){
    uint64_t n = 2000000, sum = 0;
    std::vector<uint64_t> primes = EulerUtil::primesUpTo(n);

    for(uint32_t i = 0; i < primes.size(); ++i) sum += primes[i];

    return sum;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e010() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
