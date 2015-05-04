#include <cstdint>
#include <iostream>

#include "EulerUtil.hpp"

uint64_t e015(){
    uint8_t n = 20;
    uint64_t numerator = 1, denomenator = 1;

    for(uint8_t i = 1; i <= n; ++i){
        denomenator *= i;
    }

    for(uint8_t i = n + 1; i <= 2 * n; ++i){
        numerator *= i;

        uint64_t gcd = EulerUtil::gcd(numerator, denomenator);
        numerator /= gcd;
        denomenator /= gcd;
    }

    return numerator / denomenator;
}

int main(int argc, char * argv[]){
    std::cout << e015() << std::endl;
}
