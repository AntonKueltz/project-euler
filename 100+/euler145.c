#include <stdio.h>
#include <stdlib.h>
#include <time.h>

long long reverse(long long n){
    long long rev = 0;
    
    while (n > 0){
        rev = (rev*10 + n % 10);
        n /= 10;
    }
    
    return rev;
}

int allDigitsOdd(long long n){
    while(n > 0){
        if(n % 2 == 0) return 0;
        n /= 10;
    }
    
    return 1;
}

long long reversibleNumbers(long long limit){
    long long acc = 0;
    
    for(int i = 1; i <= limit; i += 2){
        if(allDigitsOdd(i + reverse(i))){
            acc += 2;
        }
    }
    
    return acc;
}

/* compile with flag -std=c99 */
int main(int argc, char * argv[]){
    long long n = 1000000000;
    if(argc > 1)  n = atoll(argv[1]);
    
    time_t start = time(NULL);
    printf("%lld\n", reversibleNumbers(n));
    time_t finish = time(NULL);
    printf("Ran in %ld seconds\n", finish-start); 
}
