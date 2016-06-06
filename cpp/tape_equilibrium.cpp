#include "tape_equilibrium.hpp"

namespace TapeEquilibrium {

int solution(std::vector<int> &A) {
    std::vector<int>::iterator i = A.begin();
    for (; i < A.end(); i++) {
    }
    return 0;
}

int sum_to(std::vector<int> &A, std::vector<int>::iterator i) {
    std::vector<int>::iterator j = A.begin();
    int result = 0;
    for (; j < i; j++) {
        result += *j;
    }
    return result;
}

}
