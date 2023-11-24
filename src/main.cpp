#include "Exchange/ByBitAdapter.hpp"
#include "Util/TimeConverter.hpp"
#include "Database/TickerDB.hpp"

int bybit_tickers();
int database_test();

int main() {
    // database_test();
    bybit_tickers();
}

int database_test(){
    const char* connectionInfo = "host=172.21.0.2 dbname=tickerdb user=root password=root";

    TickerDB tickerDB(connectionInfo);

    if (!tickerDB.connect()) {
        std::cerr << "Failed to connect to the database. Exiting." << std::endl;
        return 1;
    }

    tickerDB.createTables();

    tickerDB.insertTicker("AAPL", "1d");

    tickerDB.insertBar(1, "2023-11-23 09:00:00", 150.5, 152.3, 149.8, 151.2, 1000, 151200.0);

    tickerDB.disconnect();

    return 0;
}

int bybit_tickers(){
    ByBitAdapter adapter;

    std::string symbol = "ETHUSD";
    std::string interval = "60";
    long long startTimestamp = 1660601600000LL; 
    long long endTimestamp = 1680608800000LL;   

    std::tm dateTime = TimeConverter::timestampToDateTime(startTimestamp);
    std::cout << "Start date and time: " << std::put_time(&dateTime, "%c") << std::endl;

    std::tm dateTime2 = TimeConverter::timestampToDateTime(endTimestamp);
    std::cout << "End date and time: " << std::put_time(&dateTime2, "%c") << std::endl;

    std::vector<std::vector<std::string>> quotes = adapter.getKlines(symbol, interval, startTimestamp, endTimestamp);

    if (!quotes.empty()) {
        adapter.printQuotes(quotes);
        std::cout << "Successfully retrieved and printed klines." << std::endl;
    } else {
        std::cerr << "Failed to retrieve klines." << std::endl;
    }
    return 0;
}