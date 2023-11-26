#include "EnvReader.hpp"

EnvReader::EnvReader(const std::string& filename) { parseEnvFile(filename); }

void EnvReader::parseEnvFile(const std::string& filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Unable to open file: " << filename << std::endl;
        return;
    }

    std::string line;
    while (std::getline(file, line)) {
        if (line.find('=') != std::string::npos) {
            size_t delimiterPos = line.find('=');
            std::string key = line.substr(0, delimiterPos);
            std::string value = line.substr(delimiterPos + 1);
            envMap[key] = value;
        }
    }

    file.close();
}

std::string EnvReader::getValue(const std::string& key) {
    auto it = envMap.find(key);
    if (it != envMap.end()) {
        return it->second;
    } else {
        std::cerr << "Key not found: " << key << std::endl;
        return "";
    }
}