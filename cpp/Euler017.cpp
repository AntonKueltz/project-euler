#include <chrono>
#include <cstdint>
#include <iostream>
#include <string>

uint8_t singleDigit(uint32_t n){
    std::string words[] = {"", "one", "two", "three", "four", "five", "six",
                           "seven", "eight", "nine"};
    return words[n].length();
}

uint8_t secondDigit(uint32_t n){
    std::string teens[] = {"", "eleven", "twelve", "thirteen", "fourteen",
                           "fifteen", "sixteen", "seventeen", "eighteen",
                           "nineteen"};
    std::string words[] = {"", "ten", "twenty", "thirty", "forty", "fifty",
                           "sixty", "seventy", "eighty", "ninety"};

    if(n > 10 && n < 20)
        return teens[n % 10].length();
    else if(n > 0)
        return words[n / 10].length();
    else
        return 0;
}

uint64_t e017(){
    uint64_t sum = 0;

    for(uint32_t i = 1; i < 1000; ++i){
        uint32_t n = i;

        while(n){
            if(n < 10){
                sum += singleDigit(n);
                n = 0;
            }
            else if(n < 100){
                sum += secondDigit(n);
                if(n > 10 && n < 20)
                    n = 0;
                else
                    n %= 10;
            }
            else if(n < 1000){
                std::string hundred = "hundred", and_ = "and";
                sum += (singleDigit(i / 100) + hundred.length());

                n %= 100;
                if(n)
                    sum += and_.length();
            }
        }
    }

    std::string oneK = "onethousand";
    sum += oneK.length();
    return sum;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e017() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
