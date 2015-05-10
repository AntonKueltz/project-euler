#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

std::vector<uint32_t> getNumAsVector(const std::string num){
    std::vector<uint32_t> digits;
    digits.reserve(50);

    for(int8_t i = (num.length() - 1); i >= 0; --i)
        digits.push_back(num[i] - '0');

    return digits;
}

void addBigNum(std::vector<uint32_t> & total, const std::vector<uint32_t> num){
    uint8_t carry = 0;

    for(uint8_t i = 0; i < num.size(); ++i){
        uint32_t sum = num[i] + total[i] + carry;
        total[i] = sum % 10;
        carry = sum / 10;
    }

    for(uint8_t j = num.size(); j < total.size() && carry; ++j){
        uint32_t sum = total[j] + carry;
        total[j] = sum % 10;
        carry = sum / 10;
    }

    if(carry) total.push_back(carry);
}

uint64_t e013(){
    std::string line;
    std::ifstream numFile("txt/p013_numbers.txt");

    std::getline(numFile, line);
    std::vector<uint32_t> total = getNumAsVector(line);

    for(uint8_t i = 0; i < 99; ++i){
        std::getline(numFile, line);
        std::vector<uint32_t> num = getNumAsVector(line);
        addBigNum(total, num);
    }

    uint64_t firstTen = 0;
    for(uint8_t i = 0; i < 10; ++i)
        firstTen = firstTen * 10 + total[total.size() - 1 - i];

    return firstTen;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e013() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
