#ifndef BYBIT_ADAPTER_H
#define BYBIT_ADAPTER_H

#include "HTTPRequest.hpp"

class ByBitAdapter : public HTTPRequest {
public:
    bool getQuotes(const std::string& url, std::vector<std::vector<std::string>>& quotes);
    void printQuotes(const std::vector<std::vector<std::string>>& quotes);
};

#endif
