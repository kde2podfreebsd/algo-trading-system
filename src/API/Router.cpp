#include "Router.hpp"

void Router::handle_get(http_request request) {
    json::value response;
    response[U("message")] = json::value::string(U("Это GET запрос"));
    request.reply(status_codes::OK, response);
}

void Router::handle_post(http_request request) {
    request.extract_json()
        .then([=](json::value body) {
            json::value response;
            response[U("message")] = json::value::string(U("Это POST запрос"));
            response[U("data")] = body;
            request.reply(status_codes::Created, response);
        })
        .wait();
}

void Router::handle_put(http_request request) {
    request.extract_json()
        .then([=](json::value body) {
            json::value response;
            response[U("message")] = json::value::string(U("Это PUT запрос"));
            response[U("data")] = body;
            request.reply(status_codes::OK, response);
        })
        .wait();
}

void Router::handle_delete(http_request request) {
    json::value response;
    response[U("message")] = json::value::string(U("Это DELETE запрос"));
    request.reply(status_codes::OK, response);
}
