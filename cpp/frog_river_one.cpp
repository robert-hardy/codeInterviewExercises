#include "frog_river_one.hpp"

#include <algorithm>
#include <vector>

int first_occurrence(int target, std::vector<int> &A);

int solution(int X, std::vector<int> &A) {
    std::vector<int> occurrences(X, -1);
    for (int i=0; i<X; i++) {
        occurrences[i] = first_occurrence(i+1, A);
    }
    int result = -1;
    for (int i=0; i<X; i++) {
        result = std::max(result, occurrences[i]);
    }
    return result;
}

int first_occurrence(int target, std::vector<int> &A) {
    std::vector<int>::iterator it;
    for (it = A.begin(); it < A.end(); it++) {
        if (*it == target) {
            return std::distance(A.begin(), it);
        }
    }
    return -1;
}
