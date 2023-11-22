#include "Exchange/ByBitAdapter.hpp"
#include <vector>

int main() {
    ByBitAdapter adapter;
    std::string url = "https://api-testnet.bybit.com/v5/market/kline?category=inverse&symbol=BTCUSD&interval=60&start=1670601600000&end=1680608800000";
    std::vector<std::vector<std::string>> quotes;

    if (adapter.getQuotes(url, quotes)) {
        adapter.printQuotes(quotes);
    } else {
        std::cerr << "Failed to retrieve quotes." << std::endl;
    }

    return 0;
}
