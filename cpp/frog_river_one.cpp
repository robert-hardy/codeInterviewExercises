#include "frog_river_one.hpp"

#include <algorithm>
#include <vector>

int first_occurrence(int target, std::vector<int> &A, int N);

int solution(int X, std::vector<int> &A, int N) {
    std::vector<int> occurrences(X, -1);
    for (int i=0; i<X; i++) {
        occurrences[i] = first_occurrence(i+1, A, N);
    }
    int result = -1;
    for (int i=0; i<X; i++) {
        result = std::max(result, occurrences[i]);
    }
    return result;
}

int first_occurrence(int target, std::vector<int> &A, int N) {
    for (int i=0; i<N; i++) {
        if (A[i] == target) {
            return i;
        }
    }
    return -1;
}
