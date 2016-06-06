#ifndef CODILITY_HPP
#define CODILITY_HPP

#include <vector>

namespace Codility1 {
    int solution(std::vector<int> &A);
}

namespace Codility2 {
    int solution(int);
}

namespace Codility3 {
    struct tree {
        int x;
        tree *l;
        tree *r;
        tree(int val) :
            x(val)
        {
            this->l = 0;
            this->r = 0;
        }
    };

    void add_left(tree *T, int val);
    void add_right(tree *T, int val);
    void path_count_helper(tree *t, int biggest_seen_so_far, int &result);
    int solution(tree *T);
}

#endif /* CODILITY_HPP */
