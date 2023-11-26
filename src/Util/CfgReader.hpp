#ifndef CFGREADER_HPP
#define CFGREADER_HPP

#include <cpprest/http_client.h>

#include <fstream>
#include <iostream>
#include <map>
#include <string>

class CfgReader {
   private:
    std::map<std::string, std::string> values;

   public:
    void readEnvFile(const std::string& filename);
    std::string getValue(const std::string& key);
    std::string getServerURI();
};

#endif
