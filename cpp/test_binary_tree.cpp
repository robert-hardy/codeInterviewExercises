#include "binary_tree.h"
#include "gtest/gtest.h"

TEST(TestNode, CreateSmallTree) {
    node *root = new node;
    root->value = 1;
    add(root, 2);
    ASSERT_EQ(root->left->value, 3);
}
