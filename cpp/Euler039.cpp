#include <chrono>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <map>

uint32_t findMaxSum(std::map<uint32_t, uint8_t> & counts){
    std::map<uint32_t, uint8_t>::iterator current = counts.begin();
    std::map<uint32_t, uint8_t>::iterator end = counts.end();
    uint32_t maxSum = 0;
    uint8_t maxCount = 0;

    for( ; current != end; ++current){
        if(current->second > maxCount){
            maxSum = current->first;
            maxCount = current->second;
        }
    }

    return maxSum;
}

uint64_t e039(){
    std::map<uint32_t, uint8_t> counts;

    for(uint32_t a = 1; a <= 333; ++a){
        for(uint32_t b = a; b <= 500; ++b){
            uint32_t csquare = a * a + b * b;
            uint32_t c = (uint32_t)sqrt(csquare);

            if(c * c == csquare && (a + b + c) <= 1000){
                if(counts.count(a + b + c))
                    counts[a + b + c]++;
                else
                    counts[a + b + c];
            }
        }
    }

    return findMaxSum(counts);
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e039() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
