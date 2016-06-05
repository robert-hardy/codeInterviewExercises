#include "linked_list.hpp"

li *make_list(std::vector<std::string> values) {
    li *result = new li(values[0]);
    return result;
}
