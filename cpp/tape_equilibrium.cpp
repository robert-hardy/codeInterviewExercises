#include "tape_equilibrium.hpp"

namespace TapeEquilibrium {

int solution(std::vector<int> &A) {
    std::vector<int>::iterator i = A.begin();
    int sum_left;
    int sum_right;
    for (; i < A.end(); i++) {
        sum_left = sum_to(A, i);
        sum_right = sum_from(A, i);
        if (sum_left == sum_right) {
            return std::distance(A.begin(), i);
        }
    }
    return -1;
}

int sum_to(std::vector<int> &A, std::vector<int>::iterator i) {
    std::vector<int>::iterator j = A.begin();
    int result = 0;
    for (; j < i; j++) {
        result += *j;
    }
    return result;
}

int sum_from(std::vector<int> &A, std::vector<int>::iterator i) {
    std::vector<int>::iterator j(i);
    j++;
    int result = 0;
    for (; j < A.end(); j++) {
        result += *j;
    }
    return result;
}

}
