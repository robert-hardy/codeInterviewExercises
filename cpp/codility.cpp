#include "codility.hpp"

namespace Codility1 {

int solution(int) {
    return 1;
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
    path_count_helper(t, result);
    return result;
}

void path_count_helper(tree *t, int &result) {
    if (!t->l && !t->r) {
        ++result;
    }
    if (t->l) {
        path_count_helper(t->l, result);
    }
    if (t->r) {
        path_count_helper(t->r, result);
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
