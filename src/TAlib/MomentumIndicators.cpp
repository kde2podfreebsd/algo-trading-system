#include "TAlib.hpp"


std::vector<double> TAlibCalculator::calculateRSI(const std::vector<std::vector<std::string>>& stringCandles, int period) {
    std::vector<std::vector<double>> candles = convertStringCandlesToDouble(stringCandles);

    std::vector<double> closePrices = extractClosePrices(candles);

    int startIdx = 0;
    int endIdx = closePrices.size() - 1;
    std::vector<double> outRSI(endIdx + 1);

    TA_RetCode retCode = TA_RSI(startIdx, endIdx, closePrices.data(), period, &startIdx, &endIdx, outRSI.data());
    if (retCode != TA_SUCCESS) {
        std::cerr << "Error calculating RSI: " << retCode << std::endl;
        return {};
    }

    return outRSI;
}

std::vector<double> TAlibCalculator::calculateADX(const std::vector<std::vector<std::string>>& stringCandles, int period) {
    std::vector<std::vector<double>> candles = convertStringCandlesToDouble(stringCandles);

    int startIdx = 0;
    int endIdx = candles[0].size() - 1;
    std::vector<double> outADX(endIdx + 1);

    TA_RetCode retCode = TA_ADX(startIdx, endIdx, candles[2].data(), candles[3].data(), candles[4].data(), period, &startIdx, &endIdx, outADX.data());
    if (retCode != TA_SUCCESS) {
        std::cerr << "Error calculating ADX: " << retCode << std::endl;
        return {};
    }

    return outADX;
}