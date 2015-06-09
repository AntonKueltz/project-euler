#include <algorithm>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <vector>

uint32_t cycleLength(uint32_t d){
    uint32_t numerator = 1;
    std::vector<uint32_t> remainders;

    while(true){
        while(numerator < d) numerator *= 10;
        numerator %= d;
        auto numIndex = find(remainders.begin(), remainders.end(), numerator);

        if(numerator == 0)
            return 0;
        else if(numIndex != remainders.end())
            return remainders.end() - numIndex;
        else
            remainders.push_back(numerator);
    }
}

uint64_t e026(){
    uint64_t longest = 0, result = 0;

    for(uint32_t d = 2; d < 1000; ++d){
        uint32_t curLength = cycleLength(d);

        if(curLength > longest){
            longest = curLength;
            result = d;
        }
    }

    return result;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e026() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
