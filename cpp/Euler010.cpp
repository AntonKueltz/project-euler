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
    std::cout << e010() << std::endl;
}
