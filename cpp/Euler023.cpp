#include <chrono>
#include <cstdint>
#include <iostream>
#include <vector>

#include "EulerUtil.hpp"

std::vector<uint32_t> abundantNumbers(uint32_t n){
    std::vector<uint32_t> abundantNums;

    for(uint32_t i = 1; i < n; ++i){
        std::vector<uint64_t> divs = EulerUtil::properDivisors(i);

        uint64_t divSum = 0;
        for(uint32_t j = 0; j < divs.size(); ++j)
            divSum += divs[j];

        if(divSum > i)
            abundantNums.push_back(i);
    }

    return abundantNums;
}

uint64_t e023(){
    uint64_t sum = 0;
    std::vector<uint32_t> abundantNums = abundantNumbers(28124);
    std::vector<bool> abundantSum(28124, false);

    for(uint32_t i = 0; i < abundantNums.size(); ++i){
        for(uint32_t j = i; j < abundantNums.size(); ++j){
            uint32_t numi = abundantNums[i], numj = abundantNums[j];

            if(numi + numj > 28123)
                break;
            else
                abundantSum[numi + numj] = true;
        }
    }

    for(uint32_t i = 1; i < abundantSum.size(); ++i){
        if(!abundantSum[i])
            sum += i;
    }

    return sum;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e023() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
