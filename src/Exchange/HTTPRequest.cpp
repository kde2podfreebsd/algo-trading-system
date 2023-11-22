#include "HTTPRequest.hpp"
#include <iostream>
#include <curl/curl.h>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

HTTPRequest::HTTPRequest() {
    curl = curl_easy_init();
    if (!curl) {
        std::cerr << "Failed to initialize curl" << std::endl;
    }
}

HTTPRequest::~HTTPRequest() {
    if (curl) {
        curl_easy_cleanup(curl);
    }
}

bool HTTPRequest::sendGETRequest(const std::string& url, std::string& response) {
    if (!curl) {
        std::cerr << "Curl not initialized" << std::endl;
        return false;
    }

    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);

    CURLcode res = curl_easy_perform(curl);
    if (res != CURLE_OK) {
        std::cerr << "curl_easy_perform() failed: " << curl_easy_strerror(res) << std::endl;
        return false;
    }

    return true;
}

bool HTTPRequest::parseJSONResponse(const std::string& jsonString, std::vector<std::vector<std::string>>& quotes) {
    json jsonResponse;
    try {
        jsonResponse = json::parse(jsonString);
    } catch (const json::parse_error& e) {
        std::cerr << "JSON parsing error: " << e.what() << std::endl;
        return false;
    }

    if (jsonResponse["retCode"] == 0) {
        json resultList = jsonResponse["result"]["list"];

        for (auto& entry : resultList) {
            std::vector<std::string> quote;
            for (const auto& item : entry) {
                quote.push_back(item);
            }
            quotes.push_back(quote);
        }

        return true;
    } else {
        std::cerr << "Request failed with error: " << jsonResponse["retMsg"] << std::endl;
        return false;
    }
}

size_t HTTPRequest::WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
    ((std::string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}
