#include "linked_list.hpp"

li::li(std::string val) : value(val) {};

li *make_list(std::vector<std::string> values) {
    li *result = new li(values[0]);
    return result;
}
