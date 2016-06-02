#ifndef BINARYTREE_H
#define BINARYTREE_H

struct Node {
    int value;
    Node *left;
    Node *right;

    Node(int val) {
        this->value = val;
        this->left = 0;
        this->right = 0;
    }
};

void add(Node *r, int val);

#endif /* BINARYTREE_H */
