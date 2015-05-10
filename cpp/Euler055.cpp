#include <chrono>
#include <cstdint>
#include <iostream>

#include "EulerUtil.hpp"

uint64_t e055(){
    uint32_t n = 10000;
    uint64_t lychrelNums = 0;

    for(uint32_t i = 0; i < n; ++i){
        uint64_t m = i;

        for(uint8_t rounds = 0; rounds < 50; ++rounds){
            m += EulerUtil::reverse(m);

            if(EulerUtil::isPalindrome(m)) break;
        }

        if(!EulerUtil::isPalindrome(m)) lychrelNums++;
    }

    return lychrelNums;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e055() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
