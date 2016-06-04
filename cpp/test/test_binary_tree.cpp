#include "gtest/gtest.h"

#include "../binary_tree.hpp"

TEST(BinaryTree, CreateSmallTree) {
    Node *tree = make_tree(1);
    add(tree, 2);
    std::string output = parse(tree);
    ASSERT_EQ(output, "12");
}

TEST(BinaryTree, ParseAndPrint) {
    Node *tree = make_tree(1);
    add(tree, 2);
    add(tree, 3);
    add(tree, 4);
    testing::internal::CaptureStdout();
    parse_print(tree);
    std::string output = testing::internal::GetCapturedStdout();
    ASSERT_EQ(output, "1243");
}

TEST(BinaryTree, ParsePrintOkayForEmptyTree) {
    Node *tree = make_tree(0);
    testing::internal::CaptureStdout();
    parse_print(tree);
    std::string output = testing::internal::GetCapturedStdout();
    ASSERT_EQ(output, "0");
}

TEST(BinaryTree, ParseWithVar) {
    Node *tree = make_tree(1);
    add(tree, 2);
    add(tree, 3);
    add(tree, 4);
    std::string output = parse(tree);
    ASSERT_EQ(output, "1243");
}
