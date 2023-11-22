#include <ta-lib/ta_libc.h>

#include <iostream>
#include <vector>

int main() {
    //example
    std::vector<double> closePrices = {17055.5, 17071, 17071.5};

    int startIdx = 0;
    int endIdx = closePrices.size() - 1;
    double outRSI[endIdx + 1];

    TA_RetCode retCode = TA_RSI(startIdx, endIdx, closePrices.data(), 14, &startIdx, &endIdx, outRSI);
    if (retCode == TA_SUCCESS) {
        std::cout << "RSI values for each candlestick: " << std::endl;
        for (int i = startIdx; i <= endIdx; ++i) {
            std::cout << "Candle " << i << ": RSI = " << outRSI[i - startIdx] << std::endl;
        }
    } else {
        std::cerr << "Error calculating RSI: " << retCode << std::endl;
    }

    return 0;
}
