CC = g++
FLAGS = -Wall -Werror -Wextra
LIBS = -lcurl -ljsoncpp -lpq -lta_lib -lcpprest -lboost_system -lboost_thread -lboost_chrono -lboost_random
SRCDIR = src
BUILDDIR = build
TARGET = $(BUILDDIR)/a.out

SRCEXT = cpp
SOURCES := $(shell find $(SRCDIR) -type f -name *.$(SRCEXT))
OBJECTS := $(patsubst $(SRCDIR)/%,$(BUILDDIR)/%,$(SOURCES:.$(SRCEXT)=.o))
CFLAGS = -c

all: build

build: $(TARGET)

$(TARGET): $(OBJECTS)
	@mkdir -p $(BUILDDIR)
	$(CC) $^ $(LIBS) -o $(TARGET)

$(BUILDDIR)/%.o: $(SRCDIR)/%.$(SRCEXT)
	@mkdir -p $(dir $@)
	$(CC) $(FLAGS) $(CFLAGS) -o $@ $<

.PHONY: clean

clean:
	@rm -rf $(BUILDDIR)

clang:
	clang-format -i $(shell find $(SRCDIR) -name "*.$(SRCEXT)") $(shell find $(SRCDIR) -name "*.hpp")
