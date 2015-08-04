#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <vector>

#include "EulerUtil.hpp"

bool isTruncatable(uint64_t prime, std::vector<uint64_t> & primes){
    if((prime % 10 != 3 && prime % 10 != 7) || prime < 10) return false;

    uint64_t n = prime / 10;
    while(n){
        if(std::binary_search(primes.begin(), primes.end(), n))
            n /= 10;
        else return false;
    }

    uint8_t scale = (uint8_t)log10(prime);
    n = prime % (uint64_t)pow(10, scale--);
    while(n){
        if(std::binary_search(primes.begin(), primes.end(), n))
            n %= (uint64_t)pow(10, scale--);
        else return false;
    }

    return true;
}


uint64_t e037(){
    uint8_t count = 0;
    uint64_t sum = 0;
    std::vector<uint64_t> primes = EulerUtil::primesUpTo(1000000);

    for(uint32_t i = 0; i < primes.size(); ++i){
        if(count == 11) return sum;

        uint64_t prime = primes[i];
        if(isTruncatable(prime, primes)){
            sum += prime;
            count++;
        }
    }

    return 0;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e037() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
