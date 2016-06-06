#include "gtest/gtest.h"

#include "../codility.hpp"

TEST(Codility1, CheckInitialization) {
    using namespace Codility1;
    int init[] = {2, 2, 2, 2, 1, 2, -1, 2, 1, 3};
    std::vector<int> A(init, init+sizeof(init)/sizeof(init[0]));
    EXPECT_EQ(A.size(), 10);
    EXPECT_EQ(A.front(), 2);
    int result = solution(A);
    ASSERT_EQ(result, 1);
}

TEST(Codility1, CheckSliceCounterReturns1) {
    using namespace Codility1;
    int init[] = {2, 2, 2, 2, 1, 2, -1, 2, 1, 3};
    std::vector<int> A(init, init+sizeof(init)/sizeof(init[0]));
    std::vector<int>::iterator i = A.begin();
    int result = count_size(A, i);
    ASSERT_EQ(result, 1);
    i++;
    int result2 = count_size(A, i);
    ASSERT_EQ(result, 1);
    ASSERT_EQ(*i, 2);
}

TEST(Codility1, CheckSliceCounterReturns2) {
    using namespace Codility1;
    int init[] = {2, 3, 2};
    std::vector<int> A(init, init+sizeof(init)/sizeof(init[0]));
    std::vector<int>::iterator i = A.begin();
    int result = count_size(A, i);
    ASSERT_EQ(result, 2);
}

TEST(Codility1, CheckSliceCounterReturns3) {
    using namespace Codility1;
    int init[] = {2, 3, 4, 2};
    std::vector<int> A(init, init+sizeof(init)/sizeof(init[0]));
    std::vector<int>::iterator i = A.begin();
    int result = count_size(A, i);
    ASSERT_EQ(result, 3);
}

TEST(Codility1, CheckFindsSliceOfLength2) {
    using namespace Codility1;
    int init[] = {2, 2, 2, 2, 1, 2, -1, 2, 1, 3};
    std::vector<int> A(init, init+sizeof(init)/sizeof(init[0]));

    std::vector<int>::iterator i = A.begin();
    i = i + 4;
    ASSERT_EQ(*i, 1);
    int slice_length = count_size(A, i);
    ASSERT_EQ(slice_length, 2);
    int result = solution(A);
    ASSERT_EQ(result, 4);
}



TEST(Codility2, GettingStarted) {
    using namespace Codility2;
    int result = solution(1);
    ASSERT_EQ(result, 2);
}

TEST(Codility3, GettingStarted) {
    using namespace Codility3;
    tree *foo = new tree(10);
    int result = solution(foo);
    ASSERT_EQ(foo->x, 10);
    ASSERT_EQ(result, 1);
}

TEST(Codility3, BuildBasicTree) {
    using namespace Codility3;
    tree *foo = new tree(10);
    add_left(foo, 13);
    add_right(foo, 23);
    ASSERT_EQ(foo->x, 10);
    ASSERT_EQ(foo->l->x, 13);
    ASSERT_EQ(foo->r->x, 23);
}

TEST(Codility3, CountNodes) {
    using namespace Codility3;
    tree *foo = new tree(10);
    add_left(foo, 13);
    add_right(foo, 23);
    ASSERT_EQ(foo->x, 10);
    ASSERT_EQ(foo->l->x, 13);
    ASSERT_EQ(foo->r->x, 23);
    int result = solution(foo);
    ASSERT_EQ(result, 3);
}

TEST(Codility3, TestCountHelper) {
    using namespace Codility3;
    tree *foo = new tree(10);
    int result = 0;
    path_count_helper(foo, 0, result);
    ASSERT_EQ(result, 1);
}

TEST(Codility3, CountVisibleNodes) {
    using namespace Codility3;
    tree *foo = new tree(10);
    add_left(foo, 13);
    add_right(foo, 9);
    ASSERT_EQ(foo->x, 10);
    ASSERT_EQ(foo->l->x, 13);
    ASSERT_EQ(foo->r->x, 9);
    int result = solution(foo);
    ASSERT_EQ(result, 2);
}
