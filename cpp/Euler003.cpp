#include <chrono>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <vector>

#include "EulerUtil.hpp"

uint64_t e003(){
    uint64_t n = 600851475143, high = 0;
    std::vector<uint64_t> primes = EulerUtil::primesUpTo(uint64_t(sqrt(n)));

    for(uint32_t i = 0; i < primes.size(); ++i){
        uint64_t prime = primes[i];

        if(n % prime == 0){
            n /= prime;
            high = prime;
        }

        if(prime > n) return high;
    }

    return high;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e003() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
