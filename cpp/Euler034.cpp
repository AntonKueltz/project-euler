#include <chrono>
#include <cstdint>
#include <iostream>

uint64_t digitFacSum(uint32_t n){
    uint64_t sum = 0;
    uint32_t factorial[] = {1, 1, 2, 6, 24, 120, 720, 540, 40320, 362880};

    while(n){
        sum += factorial[n % 10];
        n /= 10;
    }

    return sum;
}

uint64_t e034(){
    uint64_t sum = 0;

    for(uint32_t i = 3; i < 362880; ++i){
        if(i == digitFacSum(i))
            sum += i;
    }

    return sum;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e034() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
