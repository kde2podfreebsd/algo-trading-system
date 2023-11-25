#ifndef CFGREADER_HPP
#define CFGREADER_HPP

#include <fstream>
#include <iostream>
#include <map>
#include <string>

class CfgReader {
   private:
    std::map<std::string, std::string> configValues;

   public:
    void readConfigFile(const std::string& filename);
    std::string getValue(const std::string& key);
};

#endif
