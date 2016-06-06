#include "frog_river_one.hpp"

int min_index(int target, int A[], int N);

int solution(int X, int A[], int N) {
    if (X == 1) {
        return min_index(1, A, N);
    }
    return -1;
}

int min_index(int target, int A[], int N) {
    for (int i=0; i<N; i++) {
        if (A[i] == target) {
            return i;
        }
    }
    return -1;
}
