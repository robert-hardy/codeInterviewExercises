#include "gtest/gtest.h"

#include "../codility.hpp"

TEST(Codility1, GettingStarted) {
    int result = Codility1::solution(1);
    ASSERT_EQ(result, 1);
}

TEST(Codility2, GettingStarted) {
    int result = Codility2::solution(1);
    ASSERT_EQ(result, 2);
}

TEST(Codility3, GettingStarted) {
    int result = Codility3::solution(1);
    ASSERT_EQ(result, 3);
}
