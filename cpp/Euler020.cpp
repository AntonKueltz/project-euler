#include <chrono>
#include <cstdint>
#include <iostream>
#include <vector>

uint64_t e020(){
    uint64_t sum = 0;
    std::vector<uint8_t> digits;
    digits.push_back(1);

    for(uint32_t mult = 2; mult <= 100; ++mult){
        std::vector<uint8_t> tmp;

        for(uint32_t i = 0; i < digits.size(); ++i){
            uint32_t newDigits = digits[i] * mult;
            std::vector<uint8_t> meta;

            if(newDigits == 0){
                meta.push_back(0);
            }
            else{
                while(newDigits){
                    meta.push_back(newDigits % 10);
                    newDigits /= 10;
                }
            }

            uint8_t carry = 0;
            for(uint32_t j = 0; j < meta.size(); ++j){
                if(j + i < tmp.size()){
                    uint32_t newDigit = tmp[i+j] + meta[j] + carry;
                    tmp[i+j] = newDigit % 10;
                    carry = newDigit / 10;
                }
                else{
                    uint32_t newDigit = meta[j] + carry;
                    tmp.push_back(newDigit % 10);
                    carry = newDigit / 10;
                }
            }
            if(carry) tmp.push_back(carry);
        }

        digits = tmp;
    }

    for(uint32_t i = 0; i < digits.size(); ++i){
        sum += digits[i];
    }

    return sum;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e020() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
