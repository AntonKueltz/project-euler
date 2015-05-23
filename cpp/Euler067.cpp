#include <chrono>
#include <cstdint>
#include <iostream>

#include "txt/p067_triangle.cpp"

extern uint32_t triangle[];

uint64_t e067(){
    size_t triangleSize = sizeof(triangle) / sizeof(*triangle);
    uint32_t start = triangleSize - 100;

    for(uint8_t row = 99; row >= 1; --row){
        start -= row;

        for(uint32_t i = start; i < start + row; ++i){
            uint32_t left = triangle[i + row], right = triangle[i + row + 1];
            triangle[i] += (left > right ? left : right);
        }
    }

    return triangle[0];
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e067() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
