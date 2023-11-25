#ifndef TALIB_HPP
#define TALIB_HPP

#include <ta-lib/ta_libc.h>

#include <iostream>
#include <string>
#include <vector>

#include "TechIndicators/MomentumIndicators.hpp"

class TAlib {
   public:
    TAlib() {}
    ~TAlib() {}

    std::vector<double> calculateRSI(const std::vector<std::vector<std::string>>& stringCandles, int period) {
        MomentumIndicators momentum;
        return momentum.calculateRSI(stringCandles, period);
    }

    std::vector<double> calculateADX(const std::vector<std::vector<std::string>>& stringCandles, int period) {
        MomentumIndicators momentum;
        return momentum.calculateADX(stringCandles, period);
    }
};

#endif
