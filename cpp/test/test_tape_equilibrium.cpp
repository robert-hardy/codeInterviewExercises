#include "gtest/gtest.h"

#include "../tape_equilibrium.hpp"

TEST(TapeEquilibrium, GettingStarted) {
    int init[] = {1, 3, 3, 4};
    std::vector<int> A(init, init+sizeof(init)/sizeof(init[0]));
    int result = TapeEquilibrium::solution(A);
    ASSERT_EQ(result, 2);
}

