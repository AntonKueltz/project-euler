#include <chrono>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>

bool isPandigital(uint32_t i, uint32_t j, uint64_t k){
    std::vector<bool> digits(10, false);
    uint64_t vals[] = {i, j, k};

    for(uint8_t idx = 0; idx < 3; ++idx){
        uint64_t val = vals[idx];

        while(val){
            uint8_t digit = val % 10;
            if(digit == 0) return false;
            else if(digits[digit]) return false;
            else digits[digit] = true;
            val /= 10;
        }
    }

    return true;
}

uint64_t e032(){
    std::set<uint64_t> products;
    uint64_t sum = 0;

    for(uint32_t i = 2; i < 99; ++i){
        for(uint32_t j = 123; j < 9876 / 2; ++j){
            if(i < 10 && j < 1000) continue;

            uint64_t product = i * j;
            if(product > 9876) break;

            if(isPandigital(i, j, product))
                products.insert(product);
        }
    }

    for(auto it = products.begin(); it != products.end(); ++it)
        sum += *it;

    return sum;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e032() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
