#include "cyclic_rotation.hpp"

std::vector<int> solution(std::vector<int> &A, int K) {
    std::vector<int> result(A);
    if (K == 0) {
        return result;
    }
    int buffer;
    for (int i=0; i<K; i++) {
        buffer = result.back();
        result.insert(result.begin(), buffer);
        result.erase(result.end() - 1);
    }
    return result;
}
