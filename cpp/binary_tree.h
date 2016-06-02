#ifndef BINARYTREE_H
#define BINARYTREE_H

struct node {
    int value;
    node *left;
    node *right;
};

void add(node *r, int val);

struct Node {
    int value;
    Node *left;
    Node *right;

    Node(int val) {
        this->value = val;
    }
};

#endif /* BINARYTREE_H */
