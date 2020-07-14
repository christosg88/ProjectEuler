#include <vector>
#include <cmath>

std::vector<int> sieve_primes(int min, int max) {
  int sieve_bound = ((max - 1) / 2) + 1;
  int cross_limit = (((int) std::sqrt(max)) - 1) / 2;
  std::vector<bool> sieve(sieve_bound, false);
  for (int i = 1; i <= cross_limit; ++i) {
    if (!sieve[i]) {
      for (int j = 2 * i * (i + 1); j < sieve_bound; j += (2 * i) + 1) {
        sieve[j] = true;
      }
    }
  }

  std::vector<int> ret;
  ret.reserve(cross_limit);
  if (2 >= min) {
    ret.push_back(2);
  }
  for (int i = 1; i < sieve_bound; ++i) {
    int prime = 2 * i + 1;
    if (!sieve[i] && prime >= min) {
      ret.push_back(prime);
    }
  }

  return ret;
}
