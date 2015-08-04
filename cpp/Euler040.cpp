#include <chrono>
#include <cstdint>
#include <iostream>

uint64_t e040(){
    uint32_t index = 10, digits = 1, counter = 2, product = 1;

    while(index < 10000000){
        uint8_t length = 0;
        uint32_t n = counter;

        while(n){
            ++length;
            n /= 10;
        }

        if(index > digits && index <= digits + length){
            uint32_t scale = 1;
            for(uint8_t i = 0; i < length - (index - digits); ++i)
                scale *= 10;

            product *= (counter / scale) % 10;
            index *= 10;
        }

        counter++;
        digits += length;
    }

    return product;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e040() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
