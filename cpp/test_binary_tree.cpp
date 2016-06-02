#include "binary_tree.h"
#include "gtest/gtest.h"

TEST(TestNode, CreateSmallTree) {
    node *root = new node;
    root->value = 1;
    root->left = 0;
    root->right = 0;
    add(root, 2);
    ASSERT_EQ(root->left->value, 2);
}

TEST(TestNodeClass, CreateSmallTree) {
    Node *root = new Node(1);
    ASSERT_EQ(root->value, 1);
}
