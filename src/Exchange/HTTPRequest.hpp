#ifndef HTTP_REQUEST_H
#define HTTP_REQUEST_H

#include <iostream>
#include <curl/curl.h>
#include <nlohmann/json.hpp>
#include <vector>

class HTTPRequest {
public:
    HTTPRequest();
    ~HTTPRequest();
    bool sendGETRequest(const std::string& url, std::string& response);
    bool parseJSONResponse(const std::string& jsonString, std::vector<std::vector<std::string>>& quotes);

private:
    CURL* curl;
    static size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp);
};

#endif
