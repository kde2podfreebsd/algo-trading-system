#include "CfgReader.hpp"

void CfgReader::readConfigFile(const std::string& filename) {
    std::ifstream configFile(filename);

    if (!configFile.is_open()) {
        std::cerr << "Ошибка открытия файла " << filename << std::endl;
        return;
    }

    std::string line;
    while (std::getline(configFile, line)) {
        if (line.empty() || line[0] == '#') {
            continue;
        }

        size_t delimiterPos = line.find('=');
        if (delimiterPos != std::string::npos) {
            std::string key = line.substr(0, delimiterPos);
            std::string value = line.substr(delimiterPos + 1);
            value.erase(0, value.find_first_not_of(" \t\r\n"));
            value.erase(value.find_last_not_of(" \t\r\n") + 1);
            configValues[key] = value;
        }
    }

    configFile.close();
}

std::string CfgReader::getValue(const std::string& key) {
    auto it = configValues.find(key);
    if (it != configValues.end()) {
        return it->second;
    } else {
        return "";
    }
}
