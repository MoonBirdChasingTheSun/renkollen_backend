#include <string>

namespace log_line {
std::string message(std::string line) {
    std::size_t position = line.find(":");
    std::string Error_log = line.substr(position+2);
    return Error_log;
    // return the message
}

std::string log_level(std::string line) {
    std::size_t end = line.find("]");
    std::string log_Level = line.substr(1,end-1);
    return log_Level;
    // return the log level
}

std::string reformat(std::string line) {
    std::string re_format = message(line) + " (" + log_level(line) + ")" ;
    return re_format ;
    // return the reformatted message
}
}  // namespace log_line
