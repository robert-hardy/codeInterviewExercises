#include "binary_tree.h"

void add(Node *n, int val) {
    if (!n->left) {
        Node *new_node = new Node(val);
        new_node->left = 0;
        new_node->right = 0;
        n->left = new_node;
    }
}

void parse_print(Node *n) {
    std::cout << n->value;
}
