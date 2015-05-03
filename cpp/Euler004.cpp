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
    std::cout << e004() << std::endl;
}
