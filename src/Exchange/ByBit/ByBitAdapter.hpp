#ifndef BYBIT_ADAPTER_H
#define BYBIT_ADAPTER_H

#include <vector>

#include "../HTTPRequest.hpp"

class ByBitAdapter : public HTTPRequest {
   public:
    std::vector<std::vector<std::string>> getKlines(const std::string& symbol, const std::string& interval,
                                                    long long start = 0, long long end = 0);
    void printQuotes(const std::vector<std::vector<std::string>>& quotes);

   private:
    static const std::string API_URL;
};

#endif
