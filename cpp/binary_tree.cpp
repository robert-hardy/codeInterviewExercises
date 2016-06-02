#include "binary_tree.h"

void add(node *n, int val) {
    if (!n->left) {
        node *new_node = new node;
        new_node->value = val;
        n->left = new_node;
    }
}
