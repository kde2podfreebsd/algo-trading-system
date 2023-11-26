#include "CfgReader.hpp"

#include <algorithm>
#include <iterator>
#include <sstream>

void CfgReader::readEnvFile(const std::string& filename) {
    std::ifstream envFile(filename);

    if (!envFile.is_open()) {
        std::cerr << "Ошибка открытия файла " << filename << std::endl;
        return;
    }

    std::string line;
    while (std::getline(envFile, line)) {
        if (line.empty() || line[0] == '#') {
            continue;
        }

        std::istringstream iss(line);
        std::vector<std::string> tokens;
        std::copy(std::istream_iterator<std::string>(iss), std::istream_iterator<std::string>(),
                  std::back_inserter(tokens));

        if (tokens.size() >= 2) {
            std::string key = tokens[0];
            std::string value = tokens[1];

            if (value.size() >= 2 && value.front() == '"' && value.back() == '"') {
                value.erase(value.begin());  // remove leading "
                value.pop_back();            // remove trailing "
            }

            values[key] = value;

            std::cout << "Прочитано из .env: " << key << " = " << value << std::endl;
        }
    }

    envFile.close();
}

std::string CfgReader::getValue(const std::string& key) {
    auto it = values.find(key);
    if (it != values.end()) {
        return it->second;
    }
    return "";
}

std::string CfgReader::getServerURI() {
    std::string value = getValue("SERVER_URI");

    std::cout << "Значение SERVER_URI из .env: " << value << std::endl;

    if (!value.empty()) {
        try {
            web::uri uri(U(value));
            return uri.to_string();
        } catch (const web::uri_exception& e) {
            std::cerr << "Ошибка при разборе URI: " << e.what() << std::endl;
        }
    }

    return "";
}
