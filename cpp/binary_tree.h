#ifndef BINARYTREE_H
#define BINARYTREE_H

struct Node {
    int value;
    Node *left;
    Node *right;

    Node(int val) {
        this->value = val;
    }
};

void add(Node *r, int val);

#endif /* BINARYTREE_H */
