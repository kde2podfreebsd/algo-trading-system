#ifndef TIME_CONVERTER_H
#define TIME_CONVERTER_H

#include <chrono>
#include <ctime>

class TimeConverter {
   public:
    static std::tm timestampToDateTime(long long timestampMs);
    static long long dateTimeToTimestamp(const std::tm& datetime);
};

#endif
