#include <chrono>
#include <cstdint>
#include <iostream>

#include "EulerUtil.hpp"

uint64_t e182(){
    uint32_t p = 1009, q = 3643, N = p * q, phiN = (p - 1) * (q - 1);
    uint64_t bestSum = 0, lowest = N;

    for(uint32_t e = 2; e < phiN; ++e){
        if(EulerUtil::gcd(e, phiN) == 1){
            uint64_t t1, t2, unconcealed;

            t1 = EulerUtil::gcd(e-1, p-1);
            t2 = EulerUtil::gcd(e-1, q-1);
            unconcealed = (1 + t1) * (1 + t2);

            if(unconcealed < lowest){
                bestSum = e;
                lowest = unconcealed;
            }
            else if(unconcealed == lowest)
            bestSum += e;
        }
    }

    return bestSum;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e182() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
