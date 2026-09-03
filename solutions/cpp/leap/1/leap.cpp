#include "leap.h"
#include <string>
namespace leap {
int givenYear{};
std::string given_Year{" "};
bool is_leap_year(int givenYear){
    if(xyz(givenYear,given_Year) !=" "){
        return true;
    }else{
        return false;
    }
}
std::string xyz(int givenYear,std::string given_Year){     
    if(givenYear % 4 != 0){
        given_Year = given_Year;
    }else if(givenYear % 100 == 0 && givenYear % 400 != 0){
        given_Year = given_Year;
    }else{
        given_Year = "Y";
    }
    return given_Year;
}
// TODO: add your solution here

}  // namespace leap
