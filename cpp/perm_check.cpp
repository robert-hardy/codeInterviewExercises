#include "perm_check.hpp"

namespace PermCheck {

int solution(std::vector<int> &A) {
    int N = A.size();
    std::vector<bool> seen(N, false);
    std::vector<int>::iterator it = A.begin();
    for (; it < A.end(); it++) {
        if (seen[*it-1]) {
            return 0;
        }
        seen[*it-1] = true;
    }
    std::vector<bool>::iterator it2 = seen.begin();
    for (; it2 < seen.end(); it2++) {
        if (!*it2) {
            return 0;
        }
    }
    return 1;
}

}
