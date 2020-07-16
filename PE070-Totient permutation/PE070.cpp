// https://en.wikipedia.org/wiki/Euler%27s_totient_function#Euler's_product_formula

#include "../sieve.h"

#include <algorithm>
#include <array>
#include <cmath>
#include <iostream>
#include <limits>
#include <vector>

#define LIMIT 10000000

bool is_permutation(unsigned long long a, unsigned long long b) {
  if ((int) std::log10(a) != (int) std::log10(b)) {
    return false;
  }

  std::array<int, 10> a_digits{0, 0, 0, 0, 0, 0, 0, 0, 0 ,0};
  std::array<int, 10> b_digits{0, 0, 0, 0, 0, 0, 0, 0, 0 ,0};

  while (a != 0) {
    ++a_digits[a % 10];
    a /= 10;
  }
  while (b != 0) {
    ++b_digits[b % 10];
    b /= 10;
  }

  for (int i = 0; i < 10; ++i) {
    if (a_digits[i] != b_digits[i]) {
      return false;
    }
  }

  return true;
}

int main() {
  std::vector<int> primes(sieve_primes(1, LIMIT));
  int num_primes = primes.size();
  float min = std::numeric_limits<float>::max();
  int min_n = 0;

  // we know that the minimum must be for an n that has exactly two prime factors
  for (int i = 0; i < num_primes; ++i) {
    for (int j = i + 1; j < num_primes; ++j) {
      unsigned long long n = primes[i] * primes[j];
      if (n > LIMIT) {
        break;
      }
      unsigned long long phi_n = (primes[i] - 1) * (primes[j] - 1);
      float n_over_phi_n = (float) n / phi_n;
      if (n_over_phi_n < min && is_permutation(n, phi_n)) {
        min = n_over_phi_n;
        min_n = n;
      }
    }
  }

  std::cout << min_n << "\n";
}

// 8319823
