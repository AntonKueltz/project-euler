#include <cmath>
#include <cstdint>
#include <iostream>
#include <vector>

uint64_t e007(){
    uint64_t n = 1000000, primes = 0, iprime = 10001;
    std::vector<bool> isPrime (n, true);


    for(uint64_t i = 2; i < n; ++i){
        if(isPrime[i]){
            primes++;
            if(primes == iprime) return i;

            for(uint64_t m = 2; m * i < n; ++m){
                isPrime[m*i] = false;
            }
        }
    }

    return 0;
}

int main(int argc, char * argv[]){
    std::cout << e007() << std::endl;
}
