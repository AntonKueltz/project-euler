#include <cstdint>
#include <iostream>

uint64_t e002(){
    uint32_t n = 4000000, f1 = 1, f2 = 1;
    uint64_t sum = 0;

    while(f1 + f2 <= n){
        uint32_t tmp = f2;
        f2 += f1;
        f1 = tmp;

        if(!(f2 & 1)) sum += f2;
    }

    return sum;
}

int main(int argc, char * argv[]){
    std::cout << e002() << std::endl;
}
