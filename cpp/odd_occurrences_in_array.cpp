/*
   Problem found at: https://codility.com/programmers/task/odd_occurrences_in_array/
*/

#include "odd_occurrences_in_array.hpp"

#include <vector>
#include <numeric>

int my_xor(int x, int y) {
    return x^y;
}

int solution(std::vector<int> &A) {
    return std::accumulate(A.begin(), A.end(), 0, my_xor);
}
