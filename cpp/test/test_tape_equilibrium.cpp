#include "gtest/gtest.h"

#include "../tape_equilibrium.hpp"

TEST(TapeEquilibrium, BasicCase) {
    int init[] = {1, 3, 3, 4};
    std::vector<int> A(init, init+sizeof(init)/sizeof(init[0]));
    int result = TapeEquilibrium::solution(A);
    ASSERT_EQ(result, 2);
}

TEST(TapeEquilibrium, CheckSumTo) {
    int init[] = {1, 3, 3, 4};
    std::vector<int> A(init, init+sizeof(init)/sizeof(init[0]));
    std::vector<int>::iterator i = A.begin();
    i++;
    i++;
    int result = TapeEquilibrium::sum_to(A, i);
    ASSERT_EQ(result, 4);
}

TEST(TapeEquilibrium, CheckSumFrom) {
    int init[] = {1, 3, 3, 4};
    std::vector<int> A(init, init+sizeof(init)/sizeof(init[0]));
    std::vector<int>::iterator i = A.begin();
    i++;
    i++;
    int result = TapeEquilibrium::sum_from(A, i);
    ASSERT_EQ(result, 4);
}

TEST(TapeEquilibrium, CheckSumFromDoesNotDamageIterator) {
    int init[] = {1, 3, 3, 4};
    std::vector<int> A(init, init+sizeof(init)/sizeof(init[0]));
    std::vector<int>::iterator i = A.begin();
    i++;
    i++;
    int result = TapeEquilibrium::sum_from(A, i);
    ASSERT_EQ(result, 4);
    ASSERT_EQ(*i, 3);
}

TEST(TapeEquilibrium, NoSolution) {
    int init[] = {1, 3, 3, 3};
    std::vector<int> A(init, init+sizeof(init)/sizeof(init[0]));
    int result = TapeEquilibrium::solution(A);
    ASSERT_EQ(result, -1);
}

TEST(TapeEquilibrium, TestBigNumbers) {
    int init[] = {2147483648, 1, 2147483648};
    std::vector<int> A(init, init+sizeof(init)/sizeof(init[0]));
    int result = TapeEquilibrium::solution(A);
    ASSERT_EQ(result, 1);
}

TEST(TapeEquilibrium, TestLongArray) {
    std::vector<int> A(101, 1);
    ASSERT_EQ(A.size(), 101);
    int result = TapeEquilibrium::solution(A);
    ASSERT_EQ(result, 50);
}

TEST(TapeEquilibrium, TestLongArrayWithBigNumbers) {
    std::vector<int> A(11, 2147483648);
    ASSERT_EQ(A.size(), 11);
    int result = TapeEquilibrium::solution(A);
    ASSERT_EQ(result, 5);
}
