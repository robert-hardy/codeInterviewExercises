#include "linked_list.hpp"

li::li(std::string val) :
    value(val), next(0)
{};

li::li(std::string val, li *next) :
    value(val), next(next)
{};

void join(li *head, li *tail) {
    head->next = tail;
}

li *make_list(std::vector<std::string> values) {
    li *result = new li(values[0]);
    if (values.size() > 1) {
        li *new_node = new li(values[1]);
        join(result, new_node);
    }
    return result;
}
