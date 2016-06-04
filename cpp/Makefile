# Where to find the googletest code.
GTEST_DIR = /home/robert/googletest/googletest
GTEST_HEADERS = $(GTEST_DIR)/include/gtest/*.h \
                $(GTEST_DIR)/include/gtest/internal/*.h

# Where to find user code.
USER_DIR = .

# Where to find tests.
TEST_DIR = test

# Where to build the intermediate files
BUILD_DIR = build

# Flags passed to the preprocessor.
# Set Google Test's header directory as a system directory, such that
# the compiler doesn't generate warnings in Google Test headers.
CPPFLAGS += -isystem $(GTEST_DIR)/include

# Flags passed to the C++ compiler.
# To get verbose, add -v here.
CXXFLAGS += -g -Wall -Wextra -pthread

# All tests produced by this Makefile.
TESTS = $(BUILD_DIR)/test_binary_tree.o $(BUILD_DIR)/test_odd_occurrences_in_array.o

OBJECTS = $(BUILD_DIR)/binary_tree.o $(BUILD_DIR)/odd_occurrences_in_array.o

# Housekeeping targets
all : run_tests

run: run_tests
	./run_tests

clean :
	rm -f run_tests $(BUILD_DIR)/gtest.a $(BUILD_DIR)/gtest_main.a $(BUILD_DIR)/*.o

# googletest targets
GTEST_SRCS_ = $(GTEST_DIR)/src/*.cc $(GTEST_DIR)/src/*.h $(GTEST_HEADERS)

$(BUILD_DIR)/gtest-all.o : $(GTEST_SRCS_)
	$(CXX) $(CPPFLAGS) -I$(GTEST_DIR) $(CXXFLAGS) -c \
            $(GTEST_DIR)/src/gtest-all.cc -o $@

$(BUILD_DIR)/gtest_main.o : $(GTEST_SRCS_)
	$(CXX) $(CPPFLAGS) -I$(GTEST_DIR) $(CXXFLAGS) -c \
            $(GTEST_DIR)/src/gtest_main.cc -o $@

$(BUILD_DIR)/gtest.a : $(BUILD_DIR)/gtest-all.o
	$(AR) $(ARFLAGS) $@ $^

$(BUILD_DIR)/gtest_main.a : $(BUILD_DIR)/gtest-all.o $(BUILD_DIR)/gtest_main.o
	$(AR) $(ARFLAGS) $@ $^

# tests targets
$(OBJECTS): $(BUILD_DIR)/%.o: $(USER_DIR)/%.cpp
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $< -o $@

$(TESTS): $(BUILD_DIR)/%.o: $(TEST_DIR)/%.cpp
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $< -o $@

run_tests : $(BUILD_DIR)/binary_tree.o \
	$(BUILD_DIR)/odd_occurrences_in_array.o \
	$(BUILD_DIR)/test_binary_tree.o \
	$(BUILD_DIR)/test_odd_occurrences_in_array.o \
	$(BUILD_DIR)/gtest_main.a
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -lpthread $^ -o $@
