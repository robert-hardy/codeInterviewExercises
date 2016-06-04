#include "../binary_tree.h"
#include "gtest/gtest.h"

TEST(TestNodeClass, CreateSmallTree) {
    Node *root = new Node(1);
    add(root, 2);
    ASSERT_EQ(root->left->value, 2);
}

TEST(TestNodeClass, ParseAndPrint) {
    Node *root = new Node(1);
    add(root, 2);
    add(root, 3);
    add(root, 4);
    testing::internal::CaptureStdout();
    parse_print(root);
    std::string output = testing::internal::GetCapturedStdout();
    ASSERT_EQ(output, "1243");
}

TEST(TestNodeClass, ParsePrintOkayForEmptyTree) {
    Node *root = new Node(0);
    testing::internal::CaptureStdout();
    parse_print(root);
    std::string output = testing::internal::GetCapturedStdout();
    ASSERT_EQ(output, "0");
}

TEST(TestNodeClass, ParseWithVar) {
    Node *root = new Node(1);
    add(root, 2);
    add(root, 3);
    add(root, 4);
    std::string output = parse(root);
    ASSERT_EQ(output, "1243");
}
