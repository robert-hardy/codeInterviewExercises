#include "gtest/gtest.h"

#include "../codility.hpp"

TEST(Codility1, GettingStarted) {
    using namespace Codility1;
    int result = solution(1);
    ASSERT_EQ(result, 1);
}

TEST(Codility2, GettingStarted) {
    using namespace Codility2;
    int result = solution(1);
    ASSERT_EQ(result, 2);
}

TEST(Codility3, GettingStarted) {
    using namespace Codility3;
    tree *result = new tree(10);
    ASSERT_EQ(result->x, 10);
}
