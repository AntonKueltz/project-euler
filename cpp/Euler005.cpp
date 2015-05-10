#include <chrono>
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
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e005() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
