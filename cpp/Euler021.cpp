#include <chrono>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <vector>

#include "EulerUtil.hpp"

uint64_t e021(){
    uint64_t sum = 0;
    const uint32_t n = 10000;
    std::vector<uint64_t> dSums(n, 0);

    for(uint32_t i = 2; i < n; ++i){
        std::vector<uint64_t> divs = EulerUtil::divisors(i);
        uint64_t divSum = 0;

        for(uint32_t j = 0; j < divs.size(); ++j)
            divSum += divs[j];

        dSums[i] = divSum - i;

        if(dSums[i] != i && dSums[i] < i && dSums[dSums[i]] == i){
            sum += (dSums[i] + i);
        }
    }

    return sum;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e021() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
