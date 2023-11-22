#include "Exchange/ByBitAdapter.hpp"

int main() {
    ByBitAdapter adapter;

    std::string symbol = "ETHUSD";
    std::string interval = "60";
    long long startTimestamp = 1670601600000LL; 
    long long endTimestamp = 1680608800000LL;   
    int limit = 200;

    std::vector<std::vector<std::string>> quotes = adapter.getKlines(symbol, interval, startTimestamp, endTimestamp, limit);

    if (!quotes.empty()) {
        adapter.printQuotes(quotes);
        std::cout << "Successfully retrieved and printed klines." << std::endl;
    } else {
        std::cerr << "Failed to retrieve klines." << std::endl;
    }

    return 0;
}
