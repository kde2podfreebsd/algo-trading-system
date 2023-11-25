#include "Server.hpp"

Server::Server(utility::string_t url) : listener(url), router() {
    listener.support(methods::GET, std::bind(&Router::handle_get, &router, std::placeholders::_1));
    listener.support(methods::POST, std::bind(&Router::handle_post, &router, std::placeholders::_1));
    listener.support(methods::PUT, std::bind(&Router::handle_put, &router, std::placeholders::_1));
    listener.support(methods::DEL, std::bind(&Router::handle_delete, &router, std::placeholders::_1));
}

void Server::start() {
    listener.open().then([this]() { std::wcout << L"Сервер запущен\n"; }).wait();
}

void Server::stop() { listener.close().wait(); }