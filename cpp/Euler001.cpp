#include <cstdint>
#include <iostream>

uint64_t e001(){
    uint64_t n = 1000;
    uint64_t threeMults = ((n-1) / 3) * ((n-1) / 3 + 1) / 2;
    uint64_t fiveMults = ((n-1) / 5) * ((n-1) / 5 + 1) / 2;
    uint64_t fifteenMults = ((n-1) / 15) * ((n-1) / 15 + 1) / 2;

    return threeMults * 3 + fiveMults * 5 - fifteenMults * 15;
}

int main(int argc, char * argv[]){
    std::cout << e001() << std::endl;
}
