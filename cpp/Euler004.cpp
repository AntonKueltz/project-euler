#include <chrono>
#include <cmath>
#include <cstdint>
#include <iostream>

#include "EulerUtil.hpp"

uint64_t e004(){
    uint32_t n = 1000;
    uint64_t max = 0;

    for(uint32_t i = 0; i < n; ++i){
        for(uint32_t j = 0; j < n; ++j){
            if(EulerUtil::isPalindrome(i * j) && i * j > max) max = i * j;
        }
    }

    return max;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e004() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
