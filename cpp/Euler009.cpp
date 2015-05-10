#include <chrono>
#include <cmath>
#include <cstdint>
#include <iostream>

uint64_t e009(){
    uint32_t n = 1000;

    for(uint32_t a = 1; a < n / 3; ++a){
        for(uint32_t b = a + 1; b < n / 2; ++b){
            uint32_t csquare = a * a + b * b;
            uint32_t c = uint32_t(sqrt(csquare));

            if(c * c == csquare && a + b + c == 1000) return a * b * c;
        }
    }

    return 0;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e009() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
