#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX(a, b) ((a > b) ? a : b)

uint32_t d(uint32_t n, uint32_t p) {
    uint32_t e = 0;
    while(n % p == 0) {
        e++;
        n /= p;
    }
    return e;
}

uint32_t s(uint32_t p, int32_t e) {
    uint32_t x = 0;
    while(e > 0) {
        x += p;
        uint32_t x_ = x;
        while(x_ % p == 0) {
            e--;
            x_ /= p;
        }
    }
    return x;
}

int main() {
    const uint32_t N = 100000000;
    uint32_t * ns = (uint32_t *)calloc(N + 1, sizeof(uint32_t));
    uint32_t p = 2;

    while(p <= N) {
        if(ns[p] != 0) {
            p += 1;
            continue;
        }

        for(uint32_t n = p; n <= N; n += p) {
            uint32_t e = d(n, p);
            uint32_t v = s(p, e);
            ns[n] = MAX(ns[n], v);
        }

        p += 1;
    }

    uint64_t sum = 0;
    for(uint32_t i = 2; i <= N; i++) {
        sum += ns[i];
    }
    printf("%lld\n", sum);

    free(ns);
    return 0;
}
