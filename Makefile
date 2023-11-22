# g++ test.cpp -lcurl -ljsoncpp
# g++ talib.cpp -lta_lib

CC = g++
FLAGS = -Wall -Werror -Wextra

all: build

build: 
	g++ -Wall -Werror -Wextra main.cpp Exchange/HTTPRequest.cpp Exchange/ByBitAdapter.cpp Util/TimeConverter.cpp Database/TickerDB.cpp -lcurl -ljsoncpp -lpq -o ../build/a.out

clang:
	clang-format -i *.cpp
	clang-format -i *.hpp