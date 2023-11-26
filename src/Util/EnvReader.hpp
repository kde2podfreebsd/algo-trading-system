#ifndef ENV_READER_HPP
#define ENV_READER_HPP

#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>

class EnvReader {
   public:
    EnvReader(const std::string& filename);
    std::string getValue(const std::string& key);

   private:
    std::unordered_map<std::string, std::string> envMap;
    void parseEnvFile(const std::string& filename);
};

#endif