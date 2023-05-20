#include <iostream>
#include <set>

using namespace std;

int main() {
    int n, cur;
    cin >> n;
    multiset<int> stack;
    while (n--) {
        cin >> cur;
        auto it = stack.upper_bound(cur);
        if (it != stack.end()) stack.erase(it);
        stack.insert(cur);
    }
    cout << stack.size() << "\n";

    return 0;
}