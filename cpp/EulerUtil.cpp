#include "EulerUtil.hpp"

#include <cmath>
#include <iostream>

std::vector<uint64_t> EulerUtil::primesUpTo(const uint64_t & n){
    std::vector<uint64_t> primes;
    std::vector<bool> isPrime(n, true);
    primes.reserve(n / uint64_t(log(n)));

    for(uint64_t i = 2; i < n; ++i){
        if(isPrime[i]){
            primes.push_back(i);

            for(uint64_t m = 2; m * i < n; ++m){
                isPrime[m*i] = false;
            }
        }
    }

    return primes;
}

uint64_t EulerUtil::reverse(const uint64_t & n){
    uint64_t n_ = n, revn = 0;

    while(n_ > 0){
        revn = revn * 10 + n_ % 10;
        n_ /= 10;
    }

    return revn;
}

bool EulerUtil::isPalindrome(const uint64_t & n){
    return reverse(n) == n;
}

uint64_t EulerUtil::gcd(uint64_t n, uint64_t m){
    while(m != 0){
        uint64_t r = n % m;
        n = m;
        m = r;
    }

    return n;
}

uint64_t EulerUtil::numberOfDivisors(uint64_t n){
    // currently naive, TODO - implement prime based approach
    uint64_t factors = 0, root = uint64_t(sqrt(n));

    for(uint64_t i = 1; i < root; ++i){
        if(n % i == 0) factors += 2;
    }

    if(root * root == n) factors++;

    return factors;
}

std::vector<uint64_t> EulerUtil::divisors(uint64_t n){
    std::vector<uint64_t> divs;
    uint32_t root = (uint32_t)sqrt(n);
    if(root * root == n) divs.push_back(root);

    for(uint32_t i = 1; i < root; ++i){
        if(n % i == 0){
            divs.push_back(i);
            divs.push_back(n / i);
        }
    }

    return divs;
}
