#include <chrono>
#include <cstdint>
#include <iostream>

uint64_t e019(){
    const uint8_t months = 12;
    uint64_t sundays = 0, day = 0;
    uint8_t monthDays[months] = {31,28,31,30,31,30,31,31,30,31,30,31};

    for(uint32_t year = 1901; year < 2001; ++year){
        bool leapYear = (year % 4 == 0 && year % 400 != 0);

        for(uint8_t month = 0; month < months; ++month){
            if(day % 7 == 5) sundays++;
            day += monthDays[month];
            if(leapYear && month == 1) day++;
        }
    }

    return sundays;
}

int main(int argc, char * argv[]){
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << e019() << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << "Time: " << t/1000.0 << "s" << std::endl;
}
