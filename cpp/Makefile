# Where to find the googletest code.
GTEST_DIR = /home/robert/googletest/googletest
GTEST_HEADERS = $(GTEST_DIR)/include/gtest/*.h \
                $(GTEST_DIR)/include/gtest/internal/*.h
GTEST_SRCS_ = $(GTEST_DIR)/src/*.cc $(GTEST_DIR)/src/*.h $(GTEST_HEADERS)

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

# All tests.
TESTS = test_binary_tree.o test_odd_occurrences_in_array.o

# All sources.
OBJECTS = binary_tree.o odd_occurrences_in_array.o

# Housekeeping targets
all : directories run_tests

run: directories run_tests
	./run_tests

.PHONY: directories

directories: ${BUILD_DIR}

${BUILD_DIR}:
	        mkdir -p ${BUILD_DIR}

clean :
	rm -f run_tests
	rm -rf $(BUILD_DIR)

# googletest targets
gtest-all.o : $(GTEST_SRCS_)
	$(CXX) $(CPPFLAGS) -I$(GTEST_DIR) $(CXXFLAGS) -c \
            $(GTEST_DIR)/src/gtest-all.cc -o $(BUILD_DIR)/$@

gtest_main.o : $(GTEST_SRCS_)
	$(CXX) $(CPPFLAGS) -I$(GTEST_DIR) $(CXXFLAGS) -c \
            $(GTEST_DIR)/src/gtest_main.cc -o $(BUILD_DIR)/$@

gtest.a : gtest-all.o
	$(AR) $(ARFLAGS) $(BUILD_DIR)/$@ $(addprefix $(BUILD_DIR)/,$^)

gtest_main.a : gtest-all.o gtest_main.o
	$(AR) $(ARFLAGS) $(BUILD_DIR)/$@ $(addprefix $(BUILD_DIR)/,$^)

# project targets
$(OBJECTS) : %.o: $(USER_DIR)/%.cpp
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $< -o $(BUILD_DIR)/$@

$(TESTS) : %.o: $(TEST_DIR)/%.cpp
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $< -o $(BUILD_DIR)/$@

run_tests : $(OBJECTS) $(TESTS) gtest_main.a
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -lpthread $(addprefix $(BUILD_DIR)/,$^) -o $@
