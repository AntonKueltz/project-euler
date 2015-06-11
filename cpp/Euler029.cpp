#include <chrono>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <vector>

uint64_t e029(){
    std::vector<uint8_t> rootPow(101, 0);
    uint64_t sum = 0;

    for(uint8_t a = 2; a <= 100; ++a){
        uint8_t unique = 99;
        if(rootPow[a]){
            uint8_t copy = a / rootPow[a], exponent = 0;
            while(copy){
                exponent++;
                copy /= rootPow[a];
            }

            for(uint32_t i = 2 * exponent; i <= 100 * exponent; i += exponent){
                bool nonUnique = false;

                for(uint8_t j = 1; j < exponent; ++j){
                    if(i % j == 0 && i <= j * 100)
                        nonUnique = true;
                }

                if(nonUnique) unique--;
            }
        }
        else{
            for(uint8_t b = 2; b <= 100; ++b){
                uint32_t power = pow(a, b);
                if(power > 100) break;
                if(!rootPow[power]) rootPow[power] = a;
            }
        }

        sum += unique;
    }

    return sum;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e029() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
