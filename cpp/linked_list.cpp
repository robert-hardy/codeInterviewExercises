#include "linked_list.hpp"

li::li(std::string val) :
    value(val), next(0)
{};

li *make_list(std::vector<std::string> values) {
    li *result = new li(values[0]);
    result->next = new li(values[1]);
    return result;
}
