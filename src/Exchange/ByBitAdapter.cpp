#include "ByBitAdapter.hpp"
#include "../Util/TimeConverter.hpp"
#include <iostream>

const std::string ByBitAdapter::API_URL = "https://api-testnet.bybit.com/v5/market/kline?category=linear";

std::vector<std::vector<std::string>> ByBitAdapter::getKlines(const std::string& symbol, const std::string& interval, long long start, long long end, int limit) {
    std::vector<std::vector<std::string>> allQuotes;

    // Need fix limit & nextEnd calculation
    int maxLimit = 1000;

    while (start < end) {
        long long nextEnd = start + (maxLimit * std::stoll(interval) * 60000);

        if (nextEnd > end) {
            nextEnd = end;
        }

        std::string url = API_URL + "&symbol=" + symbol + "&interval=" + interval;

        if (start != 0) {
            url += "&start=" + std::to_string(start);
        }

        if (nextEnd != 0) {
            url += "&end=" + std::to_string(nextEnd);
        }

        if (limit != 0) {
            url += "&limit=" + std::to_string(maxLimit);
        }

        std::string response;
        std::vector<std::vector<std::string>> quotes;

        try {
            if (sendGETRequest(url, response)) {
                if (parseJSONResponse(response, quotes)) {
                    allQuotes.insert(allQuotes.end(), quotes.begin(), quotes.end());
                }
            }
        } catch (const std::exception& e) {
            std::cerr << "Error occurred: " << e.what() << std::endl;
            return {};
        }

        start = nextEnd;
    }

    return allQuotes;
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
