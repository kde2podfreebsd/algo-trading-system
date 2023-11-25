#ifndef TICKERDB_HPP
#define TICKERDB_HPP

#include <libpq-fe.h>

#include <iostream>
#include <string>

class TickerDB {
   public:
    TickerDB(const char* connectionInfo);
    ~TickerDB();

    bool connect();
    void disconnect();

    void createTables();
    void insertTicker(const std::string& ticker, const std::string& interval);
    void insertBar(int tickerId, const std::string& startTime, float openPrice, float highPrice,
                   float lowPrice, float closePrice, int volume, float turnover);

   private:
    PGconn* conn;
    const char* connectionInfo;
};

#endif