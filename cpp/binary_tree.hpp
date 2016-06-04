#ifndef BINARYTREE_HPP
#define BINARYTREE_HPP

#include <string>

struct Node;

Node *make_tree(int);

void add(Node *r, int val);

void parse_print(Node *r);

std::string parse(Node *r);

#endif /* BINARYTREE_HPP */
