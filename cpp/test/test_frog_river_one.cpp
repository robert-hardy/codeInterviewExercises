#include "gtest/gtest.h"

#include "../frog_river_one.hpp"

TEST(FrogRiverOne, TestRiverWide1) {
    int A[] = {1, 3, 1, 4, 2, 3, 5, 4};
    int result = solution(1, A, 8);
    ASSERT_EQ(result, 1);
}
