#include "EulerUtil.hpp"

#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>

std::vector<uint64_t> EulerUtil::primesUpTo(const uint64_t n){
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

bool EulerUtil::isPrime(const int64_t n){
    if(n < 2 || n % 2 == 0) return false;

    // TODO - Rabin Miller
    for(uint64_t i = 3; i <= uint64_t(sqrt(n)); i += 2){
        if(n % i == 0) return false;
    }

    return true;
}

uint64_t EulerUtil::reverse(const uint64_t n){
    uint64_t n_ = n, revn = 0;

    while(n_ > 0){
        revn = revn * 10 + n_ % 10;
        n_ /= 10;
    }

    return revn;
}

bool EulerUtil::isPalindrome(const uint64_t n){
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

std::vector<uint64_t> EulerUtil::properDivisors(uint64_t n){
    std::vector<uint64_t> divs;
    if(n == 1) return divs;

    divs.push_back(1);
    uint32_t root = (uint32_t)sqrt(n);

    for(uint32_t i = 2; i <= root; ++i){
        if(n % i == 0){
            divs.push_back(i);
            if(i * i != n) divs.push_back(n / i);
        }
    }

    return divs;
}

uint64_t EulerUtil::modExp(uint64_t base, uint64_t exponent, uint64_t mod){
    uint64_t result = 1;
    base = base % mod;

    while(exponent > 0){
        if(exponent & 0x1) result = (result * base) % mod;
        exponent = exponent >> 1;
        base = (base * base) % mod;
    }

    return result;
}

bool EulerUtil::isPandigital(uint64_t n, uint8_t length){
    std::vector<bool> digits(length+1, false);

    while(n){
        uint8_t digit = n % 10;
        if(digits[digit]) return false;
        if(digit == 0) return false;

        digits[digit] = true;
        n /= 10;
    }

    for(uint8_t i = 1; i < digits.size(); ++i)
        if(!digits[i]) return false;

    return true;
}
