#ifndef MOMENTUMINDICATORS_HPP
#define MOMENTUMINDICATORS_HPP

#include <ta-lib/ta_libc.h>

#include <string>
#include <vector>

#include "../TAlibHelper.hpp"

class MomentumIndicators {
   public:
    std::vector<double> calculateRSI(const std::vector<std::vector<std::string>>& stringCandles, int period);
    std::vector<double> calculateADX(const std::vector<std::vector<std::string>>& stringCandles, int period);
};

#endif
