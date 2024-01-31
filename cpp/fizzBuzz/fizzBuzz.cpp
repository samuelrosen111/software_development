#include <iostream>

int main() {
    int a, b, n;
    std::cin >> a >> b >> n;

    for (int i = 1; i <= n; ++i) {
        if (i % a == 0 && i % b == 0) {
            std::cout << "FizzBuzz\n";
        } else if (i % a == 0) {
            std::cout << "Fizz\n";
        } else if (i % b == 0) {
            std::cout << "Buzz\n";
        } else {
            std::cout << i << "\n";
        }
    }

    return 0;
}