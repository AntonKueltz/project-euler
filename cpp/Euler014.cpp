#include <chrono>
#include <cstdint>
#include <iostream>
#include <vector>

uint64_t e014(){
    uint32_t n = 1000000, longest = 0, ret = 0;
    std::vector<uint32_t> chains (n, 0);

    for(uint32_t i = 1; i < n; ++i){
        uint32_t m = i, length = 1;

        while(m != 1){
            if(m & 1) m = 3 * m + 1;
            else m /= 2;

            if(m < n && chains[m] != 0){
                length += chains[m];
                break;
            }
            else length++;
        }

        if(length > longest){
            longest = length;
            ret = i;
        }
    }

    return ret;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e014() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
