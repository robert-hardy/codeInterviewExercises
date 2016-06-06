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

int solution(tree *T) {
    return 3;
}

void path_count_helper(tree *t, int &result) {
    if (!t->l && !t->r) {
        ++result;
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
