#include "raindrops.h"
#include <string>
namespace raindrops {
    std::string convert(int number){
    std::string result = "";
    if(!(number%3)){
        result +="Pling";
    }
    if(!(number%5)){
        result +="Plang";
    }
    if(!(number%7)){
        result +="Plong";
    }
        if(result.empty()){
            result += std::to_string(number);
        }
        return result;
    }
 }    
// TODO: add your solution here

// namespace raindrops
