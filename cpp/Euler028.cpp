#include <chrono>
#include <cstdint>
#include <iostream>

uint64_t e028(){
    uint64_t sum = 1, lastElement = 1;

    for(uint32_t layer = 1; layer <= 500; ++layer){
        uint64_t base = lastElement + (layer * 2);
        sum += (base * 4) + (layer * 12);
        lastElement = base + (layer * 6);
    }

    return sum;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e028() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
