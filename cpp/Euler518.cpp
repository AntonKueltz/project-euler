#include <chrono>
#include <cstdint>
#include <iostream>
#include <vector>

#include "EulerUtil.hpp"

uint64_t e518(){
    uint64_t n = 100000000, sum = 0;
    std::vector<uint64_t> primes = EulerUtil::primesUpTo(n);
    std::vector<bool> lookup (n, false);

    for(uint32_t i = 0; i < primes.size(); ++i){
        lookup[primes[i] + 1] = true;
    }

    for(uint32_t num = 2; (num * num) < n; ++num){
        for(uint32_t base = 2; base * num * num < n; ++base){
            uint64_t c = base * num * num;
            if(!lookup[c]) continue;

            for(uint32_t denom = 1; denom < num; ++denom){
                if(EulerUtil::gcd(num, denom) != 1) continue;
                uint64_t a = base * denom * denom;
                uint64_t b = base * num * denom;

                if(lookup[a] && lookup[b])
                    sum += (a + b + c - 3);
            }
        }
    }

    return sum;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e518() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
