#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

uint64_t e022(){
    uint64_t nameSum = 0;
    std::string line;
    std::ifstream nameFile("txt/p022_names.txt");
    std::vector<std::string> names;
    names.reserve(5000);

    while(std::getline(nameFile, line, ',')){
        names.push_back(line.substr(1, line.length() - 2));
    }

    std::sort(names.begin(), names.end());

    for(uint32_t i = 0; i < names.size(); ++i){
        uint32_t nameVal = 0;

        for(uint8_t j = 0; j < names[i].length(); ++j)
            nameVal += names[i][j] - 'A' + 1;

        nameSum += nameVal * (i + 1);
    }

    return nameSum;
}

int main(int argc, char * argv[]){
    std::cout << e022() << std::endl;
}
