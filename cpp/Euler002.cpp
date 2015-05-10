#include <chrono>
#include <cstdint>
#include <iostream>

uint64_t e002(){
    uint32_t n = 4000000, f1 = 1, f2 = 1;
    uint64_t sum = 0;

    while(f1 + f2 <= n){
        uint32_t tmp = f2;
        f2 += f1;
        f1 = tmp;

        if(!(f2 & 1)) sum += f2;
    }

    return sum;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e002() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
