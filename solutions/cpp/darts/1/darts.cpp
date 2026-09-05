#include "darts.h"
#include <cmath>

namespace darts {
    int score(double x,double y){
        double distance = std::sqrt(x*x + y*y);
        if( distance <= 1){
           return 10;
        }else if(1<distance && distance<=5){
            return 5;
        }else if(5<distance&& distance<=10){
            return 1;
        }else{
            return 0;
        }
    }
    

// TODO: add your solution here

}  // namespace darts
