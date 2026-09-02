// INFO: Headers from the standard library should be inserted at the top via
#include <iostream>
#include <iomanip>
#include <cmath>

// daily_rate calculates the daily rate given an hourly rate
double daily_rate(double hourly_rate) {
    double dailyRate = 8 * hourly_rate ;
    // TODO: Implement a function to calculate the daily rate given an hourly
    // rate
    return dailyRate;
}

// apply_discount calculates the price after a discount
double apply_discount(double before_discount, double discount) {
    // TODO: Implement a function to calculate the price after a discount.
    double applyDiscount = before_discount - before_discount * (discount / 100) ;
    return applyDiscount;
}

// monthly_rate calculates the monthly rate, given an hourly rate and a discount
// The returned monthly rate is rounded up to the nearest integer.
int monthly_rate(double hourly_rate, double discount) {
    // TODO: Implement a function to calculate the monthly rate, and apply a
    // discount.
    double monthlyRate = 22*daily_rate(hourly_rate) - 22*daily_rate(hourly_rate)*(discount / 100) ;
    int monthly_Rate = std::ceil(monthlyRate) ;
    return monthly_Rate;
}

// days_in_budget calculates the number of workdays given a budget, hourly rate,
// and discount The returned number of days is rounded down (take the floor) to
// the next integer.
int days_in_budget(int budget, double hourly_rate, double discount) {
    // TODO: Implement a function that takes a budget, an hourly rate, and a
    // discount, and calculates how many complete days of work that covers.
    double daysInBudget = budget / (apply_discount(daily_rate(hourly_rate),discount)) ;
    int days_InBudget = std::floor(daysInBudget) ;
    return days_InBudget;
}
