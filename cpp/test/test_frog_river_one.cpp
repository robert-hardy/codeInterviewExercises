#include "gtest/gtest.h"

#include "../frog_river_one.hpp"

TEST(FrogRiverOne, TestRiverWide1) {
    int A[] = {1, 3, 1, 4, 2, 3, 5, 4};
    int result = solution(1, A, 8);
    ASSERT_EQ(result, 0);
}

TEST(FrogRiverOne, TestRiverWide1NotFirstIndex) {
    int A[] = {4, 3, 1, 4, 2, 3, 5, 4};
    int result = solution(1, A, 8);
    ASSERT_EQ(result, 2);
}

TEST(FrogRiverOne, TestRiverWide2) {
    int A[] = {4, 3, 1, 4, 2, 3, 5, 4};
    int result = solution(2, A, 8);
    ASSERT_EQ(result, 4);
}
