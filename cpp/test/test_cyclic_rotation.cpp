#include "gtest/gtest.h"

#include "../cyclic_rotation.hpp"

TEST(CyclicRotation, CheckInitializationOfVector) {
    int init[] = {1, 2, 3, 4};
    std::vector<int> v(init, init + sizeof(init)/sizeof(init[0]));
    ASSERT_EQ(v.front(), 1);
    ASSERT_EQ(v.back(), 4);
}
