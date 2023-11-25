#pragma once
#include <cpprest/http_listener.h>
#include "Router.h"

using namespace web;
using namespace web::http;
using namespace web::http::experimental::listener;

class Server {
public:
    Server(utility::string_t url);
    void start();
    void stop();

private:
    http_listener listener;
    Router router;
};