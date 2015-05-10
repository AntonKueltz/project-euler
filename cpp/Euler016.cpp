#include <chrono>
#include <cstdint>
#include <iostream>
#include <vector>

uint64_t e016(){
    uint64_t sum = 0;
    std::vector<uint8_t> digits;
    digits.push_back(1);

    for(uint32_t power = 1; power <= 1000; ++power){
        std::vector<uint8_t> tmp;
        bool carry = false;

        for(uint32_t i = 0; i < digits.size(); ++i){
            uint8_t newDigit = digits[i] * 2 + (carry ? 1 : 0);
            tmp.push_back(newDigit % 10);

            if(newDigit >= 10) carry = true;
            else carry = false;
        }

        if(carry) tmp.push_back(1);
        digits = tmp;
    }

    for(uint32_t i = 0; i < digits.size(); ++i)
        sum += digits[i];

    return sum;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e016() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
