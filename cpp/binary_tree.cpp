#include "binary_tree.h"

#include <boost/lexical_cast.hpp>
#include <iostream>

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


void parse_helper(Node *n, std::string &result) {
    result = result + boost::lexical_cast<std::string>(n->value);
    if (n->left) {
        parse_helper(n->left, result);
    }
    if (n->right) {
        parse_helper(n->right, result);
    }
}

std::string parse(Node *n) {
    std::string result = "";
    parse_helper(n, result);
    return result;
}
