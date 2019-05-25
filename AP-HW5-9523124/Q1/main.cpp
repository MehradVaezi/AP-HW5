#include <iostream>
#include <algorithm>
//#include <execution> // <execution> HEADER NOT FOUND!!!
#include <vector>


int main() {
    std::vector<int> vec1(100);
    std::vector<int> vec2(10);

    int i {};
    auto allocate = [&i](int& n) { i++; n += i; };

    // Part A:
    std::for_each(vec1.begin(), vec1.end(), allocate);
    i = 0;
    std::for_each(vec2.begin(), vec2.end(), allocate);

    std::cout << "Vec1: ";
    std::for_each(vec1.begin(), vec1.end(), [](const int& n){ std::cout << n << ", "; }); std::cout << "\n" << "\n";
    std::cout << "Vec2: ";
    std::for_each(vec2.begin(), vec2.end(), [](const int& n){ std::cout << n << ", "; }); std::cout << "\n" << "\n";

    // Part B:
    std::copy(begin(vec1), end(vec1), std::back_inserter(vec2));

    std::cout << "Altered Vec2: ";
    std::for_each(vec2.begin(), vec2.end(), [](const int& n){ std::cout << n << ", "; }); std::cout << "\n" << "\n";

    // Part C:
    std::vector<int> odd_vec{};
    std::copy_if(begin(vec1), end(vec1), std::back_inserter(odd_vec), [](const int& n){ return n % 2 == 1; });

    std::cout << "Odd_vec: ";
    std::for_each(odd_vec.begin(), odd_vec.end(), [](const int& n){ std::cout << n << ", "; }); std::cout << "\n" << "\n";

    // Part D:
    std::vector<int> reverse_vec{};
    std::reverse_copy(begin(vec1), end(vec1), std::back_inserter(reverse_vec));

    std::cout << "Reverse_vec: ";
    std::for_each(reverse_vec.begin(), reverse_vec.end(), [](const int& n){ std::cout << n << ", "; }); std::cout << "\n" << "\n";

    // Part E:
    // MAY NOT COMPILE IN SOME VERSIONS OF C++17!!! <execution> HEADER NOT FOUND!!!
    /*
    std::sort(begin(vec2), end(vec2));
    std::sort(std::execution::par, begin(vec2), end(vec2));

    std::cout << "Sorted Vec2: ";
    std::for_each(vec2.begin(), vec2.end(), [](const int& n){ std::cout << n << ", "; }); std::cout << "\n" << "\n";
    */

    return 0;
}