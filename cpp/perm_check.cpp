#include "perm_check.hpp"

namespace PermCheck {

int solution(std::vector<int> &A) {
    int N = A.size();
    int total_sum = 0;
    std::vector<int>::iterator it = A.begin();
    for (; it< A.end(); it++) {
        total_sum += *it;
    }
    if (total_sum != N*(N+1)/2) {
        return 0;
    }
    return 1;
}

}
