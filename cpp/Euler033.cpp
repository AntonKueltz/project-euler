#include <chrono>
#include <cstdint>
#include <iostream>

#include "EulerUtil.hpp"

bool cancels(uint32_t i, uint32_t j){
    uint8_t i1 = i / 10, i2 = i % 10, j1 = j / 10, j2 = j % 10;
    uint8_t i_ = i / EulerUtil::gcd(i, j), j_ = j / EulerUtil::gcd(i, j);

    if(i1 == j2 && i2 != 0 && j1 != 0){
        uint8_t tmpGcd = EulerUtil::gcd(i2, j1);
        if(i2 / tmpGcd == i_ && j1 / tmpGcd == j_)
            return true;
    }
    else if(i2 == j1 && i1 != 0 && j2 != 0){
        uint8_t tmpGcd = EulerUtil::gcd(i1, j2);
        if(i1 / tmpGcd == i_ && j2 / tmpGcd == j_)
            return true;
    }

    return false;
}

uint64_t e033(){
    uint32_t num = 1, denom = 1;

    for(uint32_t i = 10; i < 100; ++i){
        for(uint32_t j = i+1; j < 100; ++j){
            if(cancels(i, j)){
                num *= i;
                denom *= j;
            }
        }
    }

    return denom / EulerUtil::gcd(num, denom);
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e033() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
