#include "../binary_tree.h"
#include "../odd_occurrences_in_array.h"
#include "gtest/gtest.h"

TEST(BinaryTree, CreateSmallTree) {
    Node *root = new Node(1);
    add(root, 2);
    ASSERT_EQ(root->left->value, 2);
}

TEST(BinaryTree, ParseAndPrint) {
    Node *root = new Node(1);
    add(root, 2);
    add(root, 3);
    add(root, 4);
    testing::internal::CaptureStdout();
    parse_print(root);
    std::string output = testing::internal::GetCapturedStdout();
    ASSERT_EQ(output, "1243");
}

TEST(BinaryTree, ParsePrintOkayForEmptyTree) {
    Node *root = new Node(0);
    testing::internal::CaptureStdout();
    parse_print(root);
    std::string output = testing::internal::GetCapturedStdout();
    ASSERT_EQ(output, "0");
}

TEST(BinaryTree, ParseWithVar) {
    Node *root = new Node(1);
    add(root, 2);
    add(root, 3);
    add(root, 4);
    std::string output = parse(root);
    ASSERT_EQ(output, "1243");
}


TEST(OddOccurrencesInArray, FunctionExists) {
    static const int arr[] = {1, 1, 2, 2, 3};
    std::vector<int> A(arr, arr+5);
    int result = solution(A);
    ASSERT_EQ(result, 3);
}