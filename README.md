# README.md

* docker inspect pgdb | grep IPAddress
* sudo docker stop $(sudo docker ps -a -q)
* sudo docker rm $(sudo docker ps -a -q)
* docker-compose -f database.yaml build
* docker-compose -f database.yaml up
* g++ -Wall -Werror -Wextra main.cpp Exchange/HTTPRequest.cpp Exchange/ByBitAdapter.cpp Util/TimeConverter.cpp Database/TickerDB.cpp -lcurl -ljsoncpp -lpq -o ../build/a.out