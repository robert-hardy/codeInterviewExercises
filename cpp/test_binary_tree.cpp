#include "binary_tree.h"
#include "gtest/gtest.h"

TEST(TestNode, CanCreateNode) {
    node *root = new node;
    root->value = 10;
    ASSERT_EQ(root->value, 10);
}
