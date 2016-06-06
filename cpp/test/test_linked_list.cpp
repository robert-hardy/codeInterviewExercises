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

TEST(LinkedList, CreateManualList) {
    const char *init[] = {"hello", "there", "world"};
    std::vector<std::string> v(init, init + sizeof(init)/sizeof(init[0]));
    li *li2 = new li(v[2]);
    li *li1 = new li(v[1], li2);
    li *li0 = new li(v[0], li1);
    ASSERT_EQ(li0->value, "hello");
    ASSERT_TRUE(li0->next != NULL);
    ASSERT_EQ(li0->next->value, "there");
    ASSERT_TRUE(li0->next->next != NULL);
    ASSERT_EQ(li0->next->next->value, "world");
}

TEST(LinkedList, CreateListWithFunction) {
    const char *init[] = {"hello", "there", "happy", "world"};
    std::vector<std::string> v(init, init + sizeof(init)/sizeof(init[0]));
    li *result = make_list(v);
    ASSERT_EQ(result->value, "hello");
    ASSERT_TRUE(result->next != NULL);
    ASSERT_EQ(result->next->value, "there");
    ASSERT_TRUE(result->next->next != NULL);
    ASSERT_EQ(result->next->next->value, "happy");
    ASSERT_TRUE(result->next->next->next != NULL);
    ASSERT_EQ(result->next->next->next->value, "world");
}

TEST(LinkedList, PrintListToString) {
    const char *init[] = {"hello", "there", "happy", "world"};
    std::vector<std::string> v(init, init + sizeof(init)/sizeof(init[0]));
    li *lst = make_list(v);
    std::string result = to_string(lst);
    ASSERT_EQ(result, "hello there happy world");
}
