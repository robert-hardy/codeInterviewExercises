#include "gtest/gtest.h"

#include "../linked_list.hpp"

TEST(LinkedList, CheckCanInitializeVector) {
    const char *init[] = {"hello", "world"};
    std::vector<std::string> v(init, init + sizeof(init)/sizeof(init[0]));
    ASSERT_EQ(v[0], "hello");
    ASSERT_EQ(v[1], "world");
}

TEST(LinkedList, CreateSingletonList) {
    const char *init[] = {"hello"};
    std::vector<std::string> v(init, init + sizeof(init)/sizeof(init[0]));
    li *result = make_list(v);
    ASSERT_EQ(result->value, "hello");
    ASSERT_TRUE(result->next == NULL);
}

TEST(LinkedList, CreateLongerList) {
    const char *init[] = {"hello", "there", "world"};
    std::vector<std::string> v(init, init + sizeof(init)/sizeof(init[0]));
    li *result = make_list(v);
    ASSERT_EQ(result->value, "hello");
    ASSERT_TRUE(result->next != NULL);
    ASSERT_EQ(result->next->value, "world");
}
