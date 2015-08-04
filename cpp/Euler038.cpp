#include <chrono>
#include <cmath>
#include <cstdint>
#include <iostream>

#include "EulerUtil.hpp"

uint64_t e038(){
    uint64_t max = 0;

    for(uint32_t z = 1; z < 10000; ++z){
        uint64_t cand = 0;

        for(uint8_t n = 1; n < 10; ++n){
            if((uint8_t)ceil(log10(cand)) > 9) break;
            else if((uint8_t)ceil(log10(cand)) == 9){
                if(EulerUtil::isPandigital(cand, 9) && cand > max){
                    max = cand;
                }
                break;
            }
            else{
                uint64_t append = z * n;
                uint8_t digits = (uint8_t)ceil(log10(append));
                cand = cand * (uint64_t)pow(10, digits) + append;
            }
        }
    }

    return max;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e038() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
