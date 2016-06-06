#include "gtest/gtest.h"

#include "../cyclic_rotation.hpp"

TEST(CyclicRotation, CheckInitializationOfVector) {
    int init[] = {1, 2, 3, 4};
    std::vector<int> v(init, init + sizeof(init)/sizeof(init[0]));
    ASSERT_EQ(v.front(), 1);
    ASSERT_EQ(v.back(), 4);
}

TEST(CyclicRotation, RotateByZero) {
    int init[] = {1, 2, 3, 4};
    std::vector<int> v(init, init + sizeof(init)/sizeof(init[0]));
    std::vector<int> result = solution(v, 0);
    EXPECT_EQ(result.size(), 4);
    for (int i=0; i<4; ++i) {
        ASSERT_EQ(result[i], v[i]);
    }
}
