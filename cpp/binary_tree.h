#ifndef BINARYTREE_H
#define BINARYTREE_H

struct node {
    int value;
    node *left;
    node *right;
};

void add(node *r, int val);

#endif /* BINARYTREE_H */
