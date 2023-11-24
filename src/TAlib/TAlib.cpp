#include "TAlib.hpp"

std::vector<double> TAlibCalculator::extractClosePrices(const std::vector<std::vector<double>>& candles) {
    std::vector<double> closePrices;
    for (const auto& candle : candles) {
        if (candle.size() >= 5) {
            closePrices.push_back(candle[4]);
        }
    }
    return closePrices;
}

bool TAlibCalculator::checkValidData(const std::vector<double>& data) {
    return !data.empty();
}

std::vector<std::vector<double>> TAlibCalculator::convertStringCandlesToDouble(const std::vector<std::vector<std::string>>& stringCandles) {
    std::vector<std::vector<double>> doubleCandles;
    for (const auto& candle : stringCandles) {
        std::vector<double> doubleCandle;
        for (const auto& value : candle) {
            doubleCandle.push_back(std::stod(value));
        }
        doubleCandles.push_back(doubleCandle);
    }
    return doubleCandles;
}

