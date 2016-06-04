#include "gtest/gtest.h"

#include "../odd_occurrences_in_array.hpp"

TEST(OddOccurrencesInArray, SimpleCase1) {
    static const int arr[] = {1, 1, 2, 2, 9};
    std::vector<int> A(arr, arr+5);
    int result = solution(A);
    ASSERT_EQ(result, 9);
}

TEST(OddOccurrencesInArray, SingleNumberCase) {
    static const int arr[] = {1};
    std::vector<int> A(arr, arr+1);
    int result = solution(A);
    ASSERT_EQ(result, 1);
}
