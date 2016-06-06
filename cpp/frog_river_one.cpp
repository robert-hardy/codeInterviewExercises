#include "frog_river_one.hpp"

#include <algorithm>

int first_occurrence(int target, int A[], int N);

int solution(int X, int A[], int N) {
    if (X == 1) {
        return first_occurrence(1, A, N);
    }
    if (X == 2) {
        int first_occurrence_of_1 = first_occurrence(1, A, N);
        int first_occurrence_of_2 = first_occurrence(2, A, N);
        return std::max(first_occurrence_of_1, first_occurrence_of_2);
    }
    return -1;
}

int first_occurrence(int target, int A[], int N) {
    for (int i=0; i<N; i++) {
        if (A[i] == target) {
            return i;
        }
    }
    return -1;
}
