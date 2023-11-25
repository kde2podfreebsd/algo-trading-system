#ifndef TALIBHELPER_HPP
#define TALIBHELPER_HPP

#include <iostream>
#include <vector>

class TAlibHelper {
   public:
    std::vector<double> extractClosePrices(const std::vector<std::vector<double>>& candles);
    bool checkValidData(const std::vector<double>& data);
    std::vector<std::vector<double>> convertStringCandlesToDouble(
        const std::vector<std::vector<std::string>>& stringCandles);
};

#endif
