#include <chrono>
#include <cmath>
#include <cstdint>
#include <iostream>

#include "EulerUtil.hpp"

uint64_t e041(){
    uint64_t max = 0;
    std::vector<uint64_t> primes = EulerUtil::primesUpTo(10000000);

    for(uint32_t i = 0; i < primes.size(); ++i){
        uint64_t prime = primes[i];
        uint8_t digits = (uint8_t)ceil(log10(prime));

        if(digits == 3 || digits == 5 || digits == 6)
            continue;

        if(EulerUtil::isPandigital(prime, digits))
            max = prime;
    }

    return max;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e041() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
