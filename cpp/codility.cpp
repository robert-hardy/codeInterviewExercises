#include "codility.hpp"

#include <algorithm>

namespace Codility1 {

int solution(std::vector<int> &A) {
    std::vector<int>::iterator i = A.begin();
    int max_slice_length_so_far = 1;
    int at = 0;
    int slice_length;
    for(; i < A.end(); i++) {
        slice_length = count_size(A, i);
        if (slice_length > max_slice_length_so_far) {
            max_slice_length_so_far = slice_length;
            at = std::distance(A.begin(), i);
        }
    }
    return at;
}

int count_size(std::vector<int> &A, std::vector<int>::iterator i) {
    std::vector<int>::iterator j(i);
    int floor = *j;
    j++;
    for(; j < A.end(); j++) {
        if (*j <= floor) {
            return std::distance(i, j);
        }
        floor = *j;
    }
    return std::distance(i, A.end());
}

}

namespace Codility2 {

int solution(int) {
    return 2;
}

}

namespace Codility3 {

int solution(tree *t) {
    int result = 0;
    path_count_helper(t, t->x, result);
    return result;
}

void path_count_helper(tree *t, int biggest_seen_so_far, int &result) {
    if (t->x >= biggest_seen_so_far) {
        ++result;
    }
    int new_biggest = std::max(biggest_seen_so_far, t->x);
    if (t->l) {
        path_count_helper(t->l, new_biggest, result);
    }
    if (t->r) {
        path_count_helper(t->r, new_biggest, result);
    }
}

void add_left(tree *t, int val) {
    tree *new_node = new tree(val);
    t->l = new_node;
}

void add_right(tree *t, int val) {
    tree *new_node = new tree(val);
    t->r = new_node;
}

}
