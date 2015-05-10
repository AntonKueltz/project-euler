#include <chrono>
#include <cstdint>
#include <iostream>
#include <vector>

#include "EulerUtil.hpp"

uint64_t e512(){
    uint32_t n = 500000000;
    std::vector<uint64_t> primes = EulerUtil::primesUpTo(n+1);
    std::vector<uint64_t> totients (n+1, 0);
    for(uint32_t i = 0; i < totients.size(); ++i) totients[i] = i;
    uint64_t sum = 0;

    for(uint32_t i = 0; i < primes.size(); ++i){
        uint64_t prime = primes[i];

        for(uint32_t r = prime; r < n; r += prime)
            totients[r] = uint64_t(totients[r] * (1.0 - 1.0 / prime));
    }

    for(uint32_t i = 1; i < n+1; i += 2)
        sum += totients[i];

    return sum;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e512() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
