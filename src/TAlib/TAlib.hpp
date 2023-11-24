#ifndef TALIB_HPP
#define TALIB_HPP

#include <vector>
#include <ta-lib/ta_libc.h>
#include <iostream>

class TAlibCalculator {
public:
    std::vector<double> calculateRSI(const std::vector<std::vector<std::string>>& stringCandles, int period);
    std::vector<double> calculateADX(const std::vector<std::vector<std::string>>& stringCandles, int period);

private:
    std::vector<double> extractClosePrices(const std::vector<std::vector<double>>& candles);
    std::vector<std::vector<double>> convertStringCandlesToDouble(const std::vector<std::vector<std::string>>& stringCandles);
    bool checkValidData(const std::vector<double>& data);
};

#endif
