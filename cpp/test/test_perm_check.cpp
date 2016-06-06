#include "gtest/gtest.h"

#include "../perm_check.hpp"

TEST(PermCheck, CheckTrueCase) {
    int init[] = {1, 2, 3, 4};
    std::vector<int> A(init, init+sizeof(init)/sizeof(init[0]));
    int result = PermCheck::solution(A);
    ASSERT_EQ(result, 1);
}

TEST(PermCheck, CheckFalseCase) {
    int init[] = {1, 2, 4, 4};
    std::vector<int> A(init, init+sizeof(init)/sizeof(init[0]));
    int result = PermCheck::solution(A);
    ASSERT_EQ(result, 0);
}
