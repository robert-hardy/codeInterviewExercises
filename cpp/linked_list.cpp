#include "linked_list.hpp"

li::li(std::string val) :
    value(val), next(0)
{};

li::li(std::string val, li *next) :
    value(val), next(next)
{};

li *make_list(std::vector<std::string> values) {
    li *end = new li(values.back());
    if (values.size() == 1) {
        return end;
    }
    std::vector<std::string>::reverse_iterator rit = values.rbegin();
    ++rit;
    li *current_node = end;
    for (; rit != values.rend(); ++rit) {
        li *new_node = new li(*rit, current_node);
        current_node = new_node;
    }
    return current_node;
}

std::string to_string(li *lst) {
    return "hello";
}
