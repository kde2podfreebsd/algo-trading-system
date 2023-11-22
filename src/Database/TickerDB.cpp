#include "TickerDB.hpp"

TickerDB::TickerDB(const char* connectionInfo) : conn(nullptr), connectionInfo(connectionInfo) {}

TickerDB::~TickerDB() {
    disconnect();
}

bool TickerDB::connect() {
    conn = PQconnectdb(connectionInfo);
    if (PQstatus(conn) != CONNECTION_OK) {
        std::cerr << "Connection to database failed: " << PQerrorMessage(conn) << std::endl;
        disconnect();
        return false;
    }
    std::cout << "Connected to database!" << std::endl;
    return true;
}

void TickerDB::disconnect() {
    if (conn != nullptr) {
        PQfinish(conn);
        conn = nullptr;
        std::cout << "Disconnected from database!" << std::endl;
    }
}

void TickerDB::createTables() {
    const char* query1 = "CREATE TABLE IF NOT EXISTS tickers (id SERIAL PRIMARY KEY, ticker TEXT, interval_bar TEXT)";
    const char* query2 = "CREATE TABLE IF NOT EXISTS bars (id SERIAL PRIMARY KEY, ticker_id INT REFERENCES tickers(id), "
                         "start_time TIMESTAMP, open_price FLOAT, high_price FLOAT, low_price FLOAT, close_price FLOAT, "
                         "volume INT, turnover FLOAT)";

    PGresult *res = PQexec(conn, query1);
    if (PQresultStatus(res) != PGRES_COMMAND_OK) {
        std::cerr << "Table creation failed for tickers: " << PQerrorMessage(conn) << std::endl;
        PQclear(res);
        return;
    }
    PQclear(res);

    res = PQexec(conn, query2);
    if (PQresultStatus(res) != PGRES_COMMAND_OK) {
        std::cerr << "Table creation failed for bars: " << PQerrorMessage(conn) << std::endl;
    }
    PQclear(res);
}

void TickerDB::insertTicker(const std::string& ticker, const std::string& interval) {
    const char* query = "INSERT INTO tickers (ticker, interval_bar) VALUES ($1, $2)";
    const char* paramValues[2] = {ticker.c_str(), interval.c_str()};

    PGresult *res = PQexecParams(conn, query, 2, NULL, paramValues, NULL, NULL, 0);

    if (PQresultStatus(res) != PGRES_COMMAND_OK) {
        std::cerr << "Ticker insertion failed: " << PQerrorMessage(conn) << std::endl;
    }

    PQclear(res);
}

void TickerDB::insertBar(int tickerId, const std::string& startTime, float openPrice, float highPrice, float lowPrice, float closePrice, int volume, float turnover) {
    const char* query = "INSERT INTO bars (ticker_id, start_time, open_price, high_price, low_price, close_price, volume, turnover) "
                        "VALUES ($1, $2, $3, $4, $5, $6, $7, $8)";

    const char* paramValues[8] = {std::to_string(tickerId).c_str(), startTime.c_str(), std::to_string(openPrice).c_str(), std::to_string(highPrice).c_str(),
                                   std::to_string(lowPrice).c_str(), std::to_string(closePrice).c_str(), std::to_string(volume).c_str(),
                                   std::to_string(turnover).c_str()};

    PGresult *res = PQexecParams(conn, query, 8, NULL, paramValues, NULL, NULL, 0);

    if (PQresultStatus(res) != PGRES_COMMAND_OK) {
        std::cerr << "Bar insertion failed: " << PQerrorMessage(conn) << std::endl;
    }

    PQclear(res);
}