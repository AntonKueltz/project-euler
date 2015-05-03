#include <cstdint>
#include <iostream>

#include "EulerUtil.hpp"

uint64_t e005(){
    uint32_t n = 20;
    uint64_t product = 1;

    for(uint32_t i = 1; i < n; ++i){
        uint64_t gcd = EulerUtil::gcd(product, i);
        product *= (i / gcd);
    }

    return product;
}

int main(int argc, char * argv[]){
    std::cout << e005() << std::endl;
}
