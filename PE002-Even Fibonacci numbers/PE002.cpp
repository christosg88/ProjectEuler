#include <iostream>

int main() {
  unsigned int first = 1;
  unsigned int second = 1;
  unsigned int evens_sum = 0;

  while (second <= 4000000) {
    unsigned int sum = first + second;
    if (sum % 2 == 0) {
      evens_sum += sum;
    }

    second = first;
    first = sum;
  }

  std::cout << evens_sum << "\n";

  return 0;
}

