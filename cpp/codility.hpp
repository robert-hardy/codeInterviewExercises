#ifndef CODILITY_HPP
#define CODILITY_HPP

namespace Codility1 {
    int solution(int);
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
    int solution(tree *T);
}

#endif /* CODILITY_HPP */
