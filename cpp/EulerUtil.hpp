#include <cstdint>
#include <vector>

class EulerUtil{
public:
    static std::vector<uint64_t> primesUpTo(const uint64_t & n);
    static uint64_t reverse(const uint64_t & n);
    static bool isPalindrome(const uint64_t & n);
    static uint64_t gcd(uint64_t n, uint64_t m);
    static uint64_t numberOfDivisors(uint64_t n);
    static std::vector<uint64_t> properDivisors(uint64_t n);
    static uint64_t modExp(uint64_t base, uint64_t exponent, uint64_t mod);
};
