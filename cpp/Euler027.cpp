#include <chrono>
#include <cstdint>
#include <iostream>

#include "EulerUtil.hpp"

int64_t e027(){
    int64_t product = 0;
    uint32_t longest = 0;
    std::vector<uint64_t> bs = EulerUtil::primesUpTo(1000);

    for(auto bIterator = bs.begin(); bIterator != bs.end(); ++bIterator){
        uint64_t b = *bIterator;

        for(int64_t a = -((b+1600) / 40); a < 1000; a++){
            uint32_t n = 0;

            while(EulerUtil::isPrime(n*n + a*n + b))
                n++;

            if(n > longest){
                longest = n;
                product = a * b;
            }
        }
    }

    return product;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e027() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
