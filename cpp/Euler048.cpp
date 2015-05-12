#include <chrono>
#include <cstdint>
#include <iostream>

uint64_t e048(){
    uint64_t sum = 0;

    for(uint32_t i = 1; i <= 1000; ++i){
        uint64_t tmp = i;

        for(uint32_t j = 1; j < i; ++j){
            tmp = (tmp * i) % 10000000000;
        }

        sum = (sum + tmp) % 10000000000;
    }

    return sum;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e048() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
