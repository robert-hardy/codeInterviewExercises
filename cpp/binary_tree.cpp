#include "binary_tree.h"

void add(Node *n, int val) {
    Node *new_node = new Node(val);
    new_node->left = 0;
    new_node->right = 0;
    if (!n->left) {
        n->left = new_node;
        return;
    }
    if (!n->right) {
        n->right = new_node;
        return;
    }
    add(n->left, val);
}

void parse_print(Node *n) {
    std::cout << n->value;
    if (n->left) {
        parse_print(n->left);
    }
    if (n->right) {
        parse_print(n->right);
    }
}

std::string result;

void parse_helper(Node *n) {
    result.push_back(n->value);
    if (n->left) {
        parse_helper(n->left);
    }
    if (n->right) {
        parse_helper(n->right);
    }
}

std::string parse(Node *n) {
    result = "";
    parse_helper(n);
    return result;
}
