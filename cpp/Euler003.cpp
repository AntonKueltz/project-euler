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
    std::cout << e003() << std::endl;
}
