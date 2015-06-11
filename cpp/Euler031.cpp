#include <chrono>
#include <cstdint>
#include <iostream>

uint8_t values[] = {1, 2, 5, 10, 20, 50, 100, 200};
uint64_t combinations = 0;

void findCombination(uint8_t i, uint32_t total){
    if(total == 200) combinations++;
    else if(total < 200){
        for(uint8_t j = i; j < 8; ++j){
            findCombination(j, total + values[j]);
        }
    }
}

uint64_t e031(){
    findCombination(0, 0);
    return combinations;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e031() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
