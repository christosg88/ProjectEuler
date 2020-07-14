// https://en.wikipedia.org/wiki/Euler%27s_totient_function#Euler's_product_formula

/**
 * This is he brute force solution. A more elegant solution is presented in the PDF after solving the problem.
 */

#include "../sieve.h"

#include <algorithm>
#include <iostream>
#include <vector>

#define LIMIT 1000000

int phi(int n, std::vector<int> const &primes) {
  double prod = std::binary_search(primes.begin(), primes.end(), n) ? 1.0 - (1.0 / n) : 1.0;

  for (int const &prime : primes) {
    if (prime * prime > n) {
      break;
    } else if (n % prime == 0) {
      prod *= 1.0 - (1.0 / prime);
    }
  }
  return n * prod;
}

int main() {
  std::vector<int> primes(sieve_primes(1, LIMIT));
  float max = 0.0;
  int max_n = 0;
  for (int n = 1; n <= LIMIT; ++n) {
    float n_over_phi_n = (float) n / phi(n, primes);
    if (n_over_phi_n > max) {
      max = n_over_phi_n;
      max_n = n;
    }
  }

  std::cout << max_n << "\n";
}

// 510510
