#include "gtest/gtest.h"

#include "../frog_river_one.hpp"

TEST(FrogRiverOne, TestRiverWide1) {
    int init_A[] = {1, 3, 1, 4, 2, 3, 5, 4};
    std::vector<int> A(init_A, init_A + sizeof(A)/sizeof(A[0]));
    int result = solution(1, A);
    ASSERT_EQ(result, 0);
}

TEST(FrogRiverOne, TestRiverWide1NotFirstIndex) {
    int init_A[] = {4, 3, 1, 4, 2, 3, 5, 4};
    std::vector<int> A(init_A, init_A + sizeof(A)/sizeof(A[0]));
    int result = solution(1, A);
    ASSERT_EQ(result, 2);
}

TEST(FrogRiverOne, TestRiverWide2) {
    int init_A[] = {4, 3, 1, 4, 2, 3, 5, 4};
    std::vector<int> A(init_A, init_A + sizeof(A)/sizeof(A[0]));
    int result = solution(2, A);
    ASSERT_EQ(result, 4);
}

TEST(FrogRiverOne, GeneralCase) {
    int init_A[] = {4, 3, 5, 4, 2, 1, 5, 4};
    std::vector<int> A(init_A, init_A + sizeof(A)/sizeof(A[0]));
    int result = solution(3, A);
    ASSERT_EQ(result, 5);
}

TEST(FrogRiverOne, NotPossible) {
    int init_A[] = {1, 4, 4, 4, 4, 4, 4, 4};
    std::vector<int> A(init_A, init_A + sizeof(A)/sizeof(A[0]));
    int result = solution(2, A);
    ASSERT_EQ(result, -1);
}

TEST(FrogRiverOne, AllLeavesInSamePlace) {
    int init_A[] = {1, 2, 2, 2, 2, 2, 2, 2};
    std::vector<int> A(init_A, init_A + sizeof(A)/sizeof(A[0]));
    int result = solution(3, A);
    ASSERT_EQ(result, -1);
}

TEST(FrogRiverOne, SingleElement) {
    int init_A[] = {1};
    std::vector<int> A(init_A, init_A + sizeof(A)/sizeof(A[0]));
    int result = solution(1, A);
    ASSERT_EQ(result, 0);
}
