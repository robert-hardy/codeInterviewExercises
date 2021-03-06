#ifndef LINKEDLIST_HPP
#define LINKEDLIST_HPP

#include <string>
#include <vector>

struct li {
    std::string value;
    li *next;
    li(std::string);
    li(std::string, li *next);
};

li *make_list(std::vector<std::string>);

std::string to_string(li *);

#endif /* LINKEDLIST_HPP */
