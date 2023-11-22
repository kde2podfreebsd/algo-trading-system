#include "ByBitAdapter.hpp"
#include "../Util/TimeConverter.hpp"
#include <iostream>

const std::string ByBitAdapter::API_URL = "https://api-testnet.bybit.com/v5/market/kline?category=linear";

std::vector<std::vector<std::string>> ByBitAdapter::getKlines(const std::string& symbol, const std::string& interval, long long start, long long end, int limit) {
    std::string url = API_URL + "&symbol=" + symbol + "&interval=" + interval;

    if (start != 0) {
        url += "&start=" + std::to_string(start);
    }

    if (end != 0) {
        url += "&end=" + std::to_string(end);
    }

    if (limit != 0) {
        url += "&limit=" + std::to_string(limit);
    }

    std::string response;
    std::vector<std::vector<std::string>> quotes;
    if (sendGETRequest(url, response)) {
        if (parseJSONResponse(response, quotes)) {
            return quotes;
        }
    }
    return {};
}

void ByBitAdapter::printQuotes(const std::vector<std::vector<std::string>>& quotes) {
    TimeConverter timeConverter;

    for (const auto& quote : quotes) {
        if (quote.size() > 0) {
            long long timestamp = std::stoll(quote[0]);
            std::tm dateTime = timeConverter.timestampToDateTime(timestamp);

            std::cout << std::put_time(&dateTime, "%c") << " | ";

            for (size_t i = 1; i < quote.size(); ++i) {
                std::cout << quote[i] << " | ";
            }
            std::cout << std::endl << std::endl;
        }
    }
}



// void ByBitAdapter::printQuotes(const std::vector<std::vector<std::string>>& quotes) {
//     for (const auto& quote : quotes) {
//         for (const auto& data : quote) {
//             std::cout << data << " ";
//         }
//         std::cout << std::endl;
//     }
// }
