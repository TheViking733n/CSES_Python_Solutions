#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <cmath>

template<typename T>
class SegmentTree {
public:
    SegmentTree(const std::vector<T>& data, T defaultVal = T(), std::function<T(T, T)> func = std::max<T>) {
        _default = defaultVal;
        _func = func;
        _len = data.size();
        _size = std::pow(2, std::ceil(std::log2(_len)));

        this->data = std::vector<T>(2 * _size, defaultVal);
        std::copy(data.begin(), data.end(), this->data.begin() + _size);
        for (int i = _size - 1; i >= 1; i--) {
            this->data[i] = func(this->data[i + i], this->data[i + i + 1]);
        }
    }

    void erase(int idx) {
        (*this)[idx] = _default;
    }

    T& operator[](int idx) {
        return data[idx + _size];
    }

    void set(int idx, const T& value) {
        idx += _size;
        data[idx] = value;
        idx >>= 1;
        while (idx) {
            data[idx] = _func(data[2 * idx], data[2 * idx + 1]);
            idx >>= 1;
        }
    }

    int size() const {
        return _len;
    }

    T query(int start, int stop) {
        start += _size;
        stop += _size;

        T resLeft = _default;
        T resRight = _default;
        while (start < stop) {
            if (start & 1) {
                resLeft = _func(resLeft, data[start]);
                start += 1;
            }
            if (stop & 1) {
                stop -= 1;
                resRight = _func(data[stop], resRight);
            }
            start >>= 1;
            stop >>= 1;
        }

        return _func(resLeft, resRight);
    }

    std::string toString() {
        std::string result = "SegmentTree(";
        for (int i = _size; i < 2 * _size; i++) {
            result += std::to_string(data[i]);
            if (i < 2 * _size - 1)
                result += ", ";
        }
        result += ")";
        return result;
    }

private:
    T _default;
    std::function<T(T, T)> _func;
    int _len;
    int _size;
    std::vector<T> data;
};

int main() {
    int n, q;
    std::cin >> n >> q;

    std::vector<std::vector<int>> arr(n, std::vector<int>(1));
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i][0];
    }

    auto merge = [](const std::vector<int>& a, const std::vector<int>& b) -> std::vector<int> {
        if (a.empty())
            return b;
        if (b.empty())
            return a;

        int i = 0, j = 0;
        std::vector<int> ans;
        while (i < a.size() && j < b.size()) {
            if (a[i] < b[j]) {
                int cur = a[i];
                i++;
                if (ans.empty() || ans.back() < cur) {
                    ans.push_back(cur);
                }
            }
            else {
                int cur = b[j];
                j++;
                if (ans.empty() || ans.back() < cur) {
                    ans.push_back(cur);
                }
            }
        }

        while (i < a.size()) {
            int cur = a[i];
            i++;
            if (ans.empty() || ans.back() < cur) {
                ans.push_back(cur);
            }
        }

        while (j < b.size()) {
            int cur = b[j];
            j++;
            if (ans.empty() || ans.back() < cur) {
                ans.push_back(cur);
            }
        }

        return ans;
    };

    SegmentTree<std::vector<int>> tree(arr, std::vector<int>(), merge);

    for (int i = 0; i < q; i++) {
        int l, r;
        std::cin >> l >> r;
        l--;
        std::cout << tree.query(l, r).size() << std::endl;
    }

    return 0;
}