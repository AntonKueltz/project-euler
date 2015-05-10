#include <chrono>
#include <cstdint>
#include <iostream>

#include "EulerUtil.hpp"

bool allDigitsOdd(uint64_t n){
    while(n > 0){
        if(n % 2 == 0) return false;
        n /= 10;
    }

    return true;
}

uint64_t e145(){
    uint64_t acc = 0, n = 1000000000;

    for(uint64_t i = 1; i <= n; i += 2){
        if(allDigitsOdd(i + EulerUtil::reverse(i))){
            acc += 2;
        }
    }

    return acc;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e145() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
