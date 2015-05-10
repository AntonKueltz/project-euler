#include <chrono>
#include <cstdint>
#include <iostream>

#include "EulerUtil.hpp"

uint64_t e012(){
    uint64_t i = 1, factors = 0, triangleNum = 0;

    while(factors < 500){
        triangleNum += i;
        factors = EulerUtil::numberOfDivisors(triangleNum);
        i++;
    }

    return triangleNum;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e012() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
