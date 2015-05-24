#include <chrono>
#include <cmath>
#include <cstdint>
#include <iostream>

#include "EulerUtil.hpp"

uint64_t fakeBinary(uint32_t n){
    uint64_t bin = 0;
    uint8_t power = 0;

    while(n){
        if(n & 1)
            bin += (uint64_t)pow(10, power) * 1;

        n = n >> 1;
        power++;
    }

    return bin;
}

uint64_t e036(){
    uint64_t sum = 0;

    for(uint32_t i = 1; i < 1000000; ++i){
        uint64_t bin = fakeBinary(i);

        if(EulerUtil::reverse(i) == i && EulerUtil::reverse(bin) == bin)
            sum += i;
    }

    return sum;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e036() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
