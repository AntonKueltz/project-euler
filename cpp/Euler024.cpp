#include <chrono>
#include <cstdint>
#include <iostream>
#include <vector>

uint64_t e024(){
    uint64_t finalNum = 0;
    int32_t fac[] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};
    int32_t n = 1000000;
    std::vector<uint8_t> availableDigits;

    for(uint8_t i = 0; i < 10; ++i)
        availableDigits.push_back(i);

    for(uint8_t digit = 0; digit < 10; ++digit){
        uint8_t digitIndex = 0;

        while(n - fac[9 - digit] > 0){
            digitIndex++;
            n -= fac[9 - digit];
        }

        finalNum = (finalNum * 10) + availableDigits[digitIndex];
        availableDigits.erase(availableDigits.begin() + digitIndex);
    }

    return finalNum;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e024() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
