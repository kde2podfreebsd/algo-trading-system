CC = g++
FLAGS = -Wall -Werror -Wextra
BUILD_FLAGS = -L$(VCPKG_DIR)/lib -lcpprest -lboost_system -lboost_thread -lboost_chrono -lboost_random -lcurl -ljsoncpp -lpq -lta_lib -lssl -lcrypto
SRCDIR = src
BUILDDIR = build
INCLUDE_DIR = include
TARGET = $(BUILDDIR)/a.out
VCPKG_DIR = $(INCLUDE_DIR)/vcpkg/installed/x64-linux

SRCEXT = cpp
SOURCES := $(shell find $(SRCDIR) -type f -name *.$(SRCEXT))
OBJECTS := $(patsubst $(SRCDIR)/%,$(BUILDDIR)/%,$(SOURCES:.$(SRCEXT)=.o))
CFLAGS = -c

all: build

build: $(TARGET)

$(TARGET): $(OBJECTS)
	@mkdir -p $(BUILDDIR)
	$(CC) $^ $(BUILD_FLAGS) -o $(TARGET)

$(BUILDDIR)/%.o: $(SRCDIR)/%.$(SRCEXT)
	@mkdir -p $(dir $@)
	$(CC) $(FLAGS) $(CFLAGS) -o $@ $< -I$(VCPKG_DIR)/include

.PHONY: clean

clean:
	@rm -rf $(BUILDDIR)

clang:
	clang-format -n $(shell find $(SRCDIR) -name "*.$(SRCEXT)") $(shell find $(SRCDIR) -name "*.hpp")
	clang-format -i $(shell find $(SRCDIR) -name "*.$(SRCEXT)") $(shell find $(SRCDIR) -name "*.hpp")

cppcheck:
	cppcheck --enable=all --suppress=missingIncludeSystem $(SRCDIR)

precommit:
	pre-commit run --all-files

docker_clean:
	sudo docker stop $$(sudo docker ps -a -q) || true
	sudo docker rm $$(sudo docker ps -a -q) || true

database_up:
	docker-compose -f database.yaml up