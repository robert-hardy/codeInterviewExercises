#include "gtest/gtest.h"

#include "../perm_check.hpp"

#include <algorithm>
#include <numeric>

TEST(PermCheck, CheckTrueCase1) {
    int init[] = {1, 2, 3, 4};
    std::vector<int> A(init, init+sizeof(init)/sizeof(init[0]));
    int result = PermCheck::solution(A);
    ASSERT_EQ(result, 1);
}

TEST(PermCheck, CheckTrueCase2) {
    int init[] = {1, 2, 3, 4, 5, 6, 7};
    std::vector<int> A(init, init+sizeof(init)/sizeof(init[0]));
    int result = PermCheck::solution(A);
    ASSERT_EQ(result, 1);
}

TEST(PermCheck, CheckTrueCaseBigArray) {
    std::vector<int> A(1000, 1);
    std::partial_sum(A.begin(), A.end(), A.begin());
    int result = PermCheck::solution(A);
    ASSERT_EQ(result, 1);
}

TEST(PermCheck, CheckTrueCaseBigArrayShuffled) {
    std::vector<int> A(1000, 1);
    std::partial_sum(A.begin(), A.end(), A.begin());
    std::random_shuffle(A.begin(), A.end());
    int result = PermCheck::solution(A);
    ASSERT_EQ(result, 1);
}

TEST(PermCheck, CheckFalseCase) {
    int init[] = {1, 2, 4, 4};
    std::vector<int> A(init, init+sizeof(init)/sizeof(init[0]));
    int result = PermCheck::solution(A);
    ASSERT_EQ(result, 0);
}
