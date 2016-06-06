#include "frog_river_one.hpp"

int solution(int X, int A[], int N) {
    if (X == 1) {
        for (int i=0; i<N; i++) {
            if (A[i] == 1) {
                return i;
            }
        }
    }
    return -1;
}
