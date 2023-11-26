#include "API/Server.hpp"
#include "Database/TickerDB.hpp"
#include "Exchange/ByBit/ByBitAdapter.hpp"
#include "TAlib/TAlib.hpp"
#include "Util/CfgReader.hpp"
#include "Util/TimeConverter.hpp"

int bybit_tickers();
int database_test();
void test_talib();
void API_test();

int main() {
    API_test();
    // database_test();
    // test_talib();
    // bybit_tickers();
}

void API_test() {
    CfgReader reader;
    reader.readEnvFile(".env");

    std::string uri = reader.getServerURI();

    if (!uri.empty()) {
        std::cout << "URI сервера: " << uri << std::endl;
    } else {
        std::cout << "Ошибка получения URI сервера" << std::endl;
        return;
    }

    Server server(uri);

    server.start();

    std::cout << "Сервер запущен. Нажмите Enter для завершения работы." << std::endl;
    std::string line;
    std::getline(std::cin, line);
    server.stop();
}

void test_talib() {
    ByBitAdapter adapter;

    std::string symbol = "ETHUSD";
    std::string interval = "60";
    long long startTimestamp = 1660601600000LL;
    long long endTimestamp = 1680608800000LL;

    std::vector<std::vector<std::string>> candles =
        adapter.getKlines(symbol, interval, startTimestamp, endTimestamp);

    TAlib talib;

    // RSi
    int rsiperiod = 14;

    std::vector<double> rsiValues = talib.calculateRSI(candles, rsiperiod);

    std::cout << "RSI values for each candlestick: " << std::endl;
    for (size_t i = 0; i < rsiValues.size(); ++i) {
        std::cout << "Candle " << i + 1 << ": RSI = " << rsiValues[i] << std::endl;
    }

    // ADX

    int adxPeriod = 14;

    std::vector<double> adxValues = talib.calculateADX(candles, adxPeriod);

    std::cout << "ADX values for each candlestick: " << std::endl;
    for (size_t i = 0; i < adxValues.size(); ++i) {
        std::cout << "Candle " << i + 1 << ": ADX = " << adxValues[i] << std::endl;
    }
}

int database_test() {
    const char* connectionInfo = "host=172.22.0.3 dbname=tickerdb user=root password=root";

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

int bybit_tickers() {
    ByBitAdapter adapter;

    std::string symbol = "ETHUSD";
    std::string interval = "60";
    long long startTimestamp = 1660601600000LL;
    long long endTimestamp = 1680608800000LL;

    std::tm dateTime = TimeConverter::timestampToDateTime(startTimestamp);
    std::cout << "Start date and time: " << std::put_time(&dateTime, "%c") << std::endl;

    std::tm dateTime2 = TimeConverter::timestampToDateTime(endTimestamp);
    std::cout << "End date and time: " << std::put_time(&dateTime2, "%c") << std::endl;

    std::vector<std::vector<std::string>> quotes =
        adapter.getKlines(symbol, interval, startTimestamp, endTimestamp);

    if (!quotes.empty()) {
        adapter.printQuotes(quotes);
        std::cout << "Successfully retrieved and printed klines." << std::endl;
    } else {
        std::cerr << "Failed to retrieve klines." << std::endl;
    }
    return 0;
}