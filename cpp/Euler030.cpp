#include <chrono>
#include <cstdint>
#include <iostream>

uint64_t fifthPow(uint32_t n){
    return n * n * n * n * n;
}

uint64_t digitFithPower(uint64_t n){
    uint64_t sum = 0;

    while(n){
        sum += fifthPow(n % 10);
        n /= 10;
    }

    return sum;
}

uint64_t e030(){
    uint64_t sum = 0;

    for(uint32_t i = 2; i <= fifthPow(9) * 5; ++i){
        if(i == digitFithPower(i))
            sum += i;
    }

    return sum;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e030() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
