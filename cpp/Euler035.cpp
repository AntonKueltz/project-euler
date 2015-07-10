#include <chrono>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <vector>

#include "EulerUtil.hpp"

uint8_t digitCount(uint64_t n){
    uint8_t digits = 0;

    while(n){
        digits++;
        n /= 10;
    }

    return digits;
}

uint64_t rotate(uint64_t n, uint8_t digits){
    uint64_t scale = (uint64_t)pow(10, digits-1);
    uint8_t first = n / scale;
    uint64_t end = n % scale;
    return end * 10 + first;
}

uint64_t e035(){
    uint32_t count = 0;
    std::vector<uint64_t> primes = EulerUtil::primesUpTo(1000000);

    std::vector<bool> lookup(1000000, false);
    for(uint32_t i = 0; i < primes.size(); ++i) lookup[primes[i]] = true;

    for(uint32_t i = 0; i < primes.size(); ++i){
        uint64_t prime = primes[i];
        uint8_t digits = digitCount(prime);
        bool circular = true;

        for(uint8_t j = 0; j < digits; ++j){
            if(!lookup[prime]){
                circular = false;
                break;
            }
            else prime = rotate(prime, digits);
        }

        if(circular) count++;
    }

    return count;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e035() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
