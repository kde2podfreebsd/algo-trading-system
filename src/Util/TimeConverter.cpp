#include "TimeConverter.hpp"

std::tm TimeConverter::timestampToDateTime(long long timestampMs) {
    std::time_t t = static_cast<std::time_t>(timestampMs / 1000);
    return *std::localtime(&t);
}

long long TimeConverter::dateTimeToTimestamp(const std::tm& datetime) {
    std::tm timeCopy = datetime;
    std::time_t time = std::mktime(&timeCopy);
    auto ms = std::chrono::milliseconds(time * 1000);
    return ms.count();
}

/*

long long timestamp = 1670601600000;

std::tm dateTime = TimeConverter::timestampToDateTime(timestamp);
std::cout << "Date and time: " << std::put_time(&dateTime, "%c") << std::endl;

long long newTimestamp = TimeConverter::dateTimeToTimestamp(dateTime);
std::cout << "Timestamp: " << newTimestamp << " ms" << std::endl;

*/