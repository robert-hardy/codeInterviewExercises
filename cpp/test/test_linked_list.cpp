#include "gtest/gtest.h"

#include "../linked_list.hpp"

TEST(LinkedList, CheckCanInitializeVector) {
    const char *init[] = {"hello", "world"};
    std::vector<std::string> v(init, init + sizeof(init)/sizeof(init[0]));
    ASSERT_EQ(v[0], "hello");
    ASSERT_EQ(v[1], "world");
}
