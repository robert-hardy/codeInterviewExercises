#include "binary_tree.h"

void add(node *n, int val) {
    if (!n->left) {
        node *new_node = new node;
        new_node->value = val;
        new_node->left = 0;
        new_node->right = 0;
        n->left = new_node;
    }
}
