#include <chrono>
#include <cstdint>
#include <iostream>
#include <vector>

void addBigNum(std::vector<uint32_t> & total, const std::vector<uint32_t> num){
    uint8_t carry = 0;

    for(uint32_t i = 0; i < num.size(); ++i){
        uint32_t sum = num[i] + total[i] + carry;
        total[i] = sum % 10;
        carry = sum / 10;
    }

    for(uint32_t j = num.size(); j < total.size() && carry; ++j){
        uint32_t sum = total[j] + carry;
        total[j] = sum % 10;
        carry = sum / 10;
    }

    if(carry) total.push_back(carry);
}

uint64_t e025(){
    uint32_t fibIndex = 2;
    std::vector<uint32_t> curFib(1,1);
    std::vector<uint32_t> lastFib(1,1);

    while(curFib.size() != 1000){
        std::vector<uint32_t> tmp(curFib);
        addBigNum(curFib, lastFib);
        lastFib = tmp;
        fibIndex++;
    }

    return fibIndex;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e025() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
