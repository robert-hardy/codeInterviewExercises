#include "gtest/gtest.h"

#include "../odd_occurrences_in_array.h"

TEST(OddOccurrencesInArray, FunctionExists) {
    static const int arr[] = {1, 1, 2, 2, 3};
    std::vector<int> A(arr, arr+5);
    int result = solution(A);
    ASSERT_EQ(result, 3);
}
