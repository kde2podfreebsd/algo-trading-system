#include "ByBitAdapter.hpp"
#include <iostream>

bool ByBitAdapter::getQuotes(const std::string& url, std::vector<std::vector<std::string>>& quotes) {
    std::string response;
    if (sendGETRequest(url, response)) {
        return parseJSONResponse(response, quotes);
    }
    return false;
}

void ByBitAdapter::printQuotes(const std::vector<std::vector<std::string>>& quotes) {
    for (const auto& quote : quotes) {
        for (const auto& data : quote) {
            std::cout << data << " ";
        }
        std::cout << std::endl;
    }
}
