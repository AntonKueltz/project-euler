#include <chrono>
#include <cstdint>
#include <iostream>

uint64_t e018(){
    uint32_t triangle[] = {
        75,
        95, 64,
        17, 47, 82,
        18, 35, 87, 10,
        20,  4, 82, 47, 65,
        19,  1, 23, 75,  3, 34,
        88,  2, 77, 73,  7, 63, 67,
        99, 65,  4, 28,  6, 16, 70, 92,
        41, 41, 26, 56, 83, 40, 80, 70, 33,
        41, 48, 72, 33, 47, 32, 37, 16, 94, 29,
        53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,
        70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,
        91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,
        63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,
         4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23
    };
    size_t triangleSize = sizeof(triangle) / sizeof(*triangle);
    uint32_t start = triangleSize - 15;

    for(uint8_t row = 14; row >= 1; --row){
        start -= row;

        for(uint8_t i = start; i < start + row; ++i){
            uint32_t left = triangle[i + row], right = triangle[i + row + 1];
            triangle[i] += (left > right ? left : right);
        }
    }

    return triangle[0];
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e018() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
