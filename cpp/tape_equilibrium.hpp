#ifndef TAPEEQUILIBRIUM_HPP
#define TAPEEQUILIBRIUM_HPP

#include <vector>

namespace TapeEquilibrium {
    int solution(std::vector<int> &A);
    long long sum_to(std::vector<int> &A, std::vector<int>::iterator i);
    long long sum_from(std::vector<int> &A, std::vector<int>::iterator i);
}

#endif /* TAPEEQUILIBRIUM_HPP*/
