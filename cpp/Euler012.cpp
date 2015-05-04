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
    std::cout << e012() << std::endl;
}
