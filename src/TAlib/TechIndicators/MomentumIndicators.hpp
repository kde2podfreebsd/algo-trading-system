#ifndef MOMENTUMINDICATORS_HPP
#define MOMENTUMINDICATORS_HPP

#include <vector>
#include <string>
#include "TAlibHelper.hpp"
#include <ta-lib/ta_libc.h>

class MomentumIndicators {
public:
    std::vector<double> calculateRSI(const std::vector<std::vector<std::string>>& stringCandles, int period);
    std::vector<double> calculateADX(const std::vector<std::vector<std::string>>& stringCandles, int period);

};

#endif
