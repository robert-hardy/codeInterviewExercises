#ifndef LINKEDLIST_HPP
#define LINKEDLIST_HPP

#include <string>
#include <vector>

struct li {
    std::string value;
    li(std::string);
};

li *make_list(std::vector<std::string>);

#endif /* LINKEDLIST_HPP */
