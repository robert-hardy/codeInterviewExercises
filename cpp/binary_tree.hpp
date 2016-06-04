#ifndef BINARYTREE_HPP
#define BINARYTREE_HPP

#include <string>

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

void parse_print(Node *r);

std::string parse(Node *r);

#endif /* BINARYTREE_HPP */
