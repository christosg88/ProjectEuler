#include <algorithm>
#include <iostream>
#include <vector>
#include <array>
#include <sstream>

using triplet = std::array<int, 3>;
using solution = std::array<triplet, 5>;

/**
 * Return true if the given arrangement is a valid solution, else false.
 */
bool is_valid_solution(std::array<int, 10> const &nums) {
  // because the valid solutions contain 16 digits, and if 10 appears more than once we have 17 digits, all valid
  // solutions have the 10 in indexes [0, 4]
  bool ten_found = false;
  for (int i = 0; i < 5; ++i) {
    if (nums[i] == 10) {
      ten_found = true;
      break;
    }
  }

  if (!ten_found) {
    return false;
  }

  int sum = nums[0] + nums[5] + nums[6];
  for (int i = 1; i < 5; ++i) {
    int part_sum = nums[i] + nums[i + 5] + nums[((i + 1) % 5) + 5];
    if (part_sum != sum) {
      return false;
    }
  }

  return true;
}

/**
 * Return true if rhs is greater than lhs, else false.
 */
bool sol_cmp(solution const &lhs, solution const &rhs) {
  // find the index of the triplet with min outer number
  int lhs_min_idx = 0;
  int lhs_min_val = lhs[0][0];
  int rhs_min_idx = 0;
  int rhs_min_val = rhs[0][0];

  for (int i = 1; i < 5; ++i) {
    if (lhs[i][0] < lhs_min_val) {
      lhs_min_idx = i;
      lhs_min_val = lhs[i][0];
    }
    if (rhs[i][0] < rhs_min_val) {
      rhs_min_idx = i;
      rhs_min_val = rhs[i][0];
    }
  }

  // create string representations of the solutions, putting the triplets in a clockwise order starting from the triplet
  // with the minimum outer number
  std::stringstream lhs_ss;
  for (int i = 0; i < 5; ++i) {
    for (int const &num : lhs[(i + lhs_min_idx) % 5]) {
      lhs_ss << num;
    }
  }

  std::stringstream rhs_ss;
  for (int i = 0; i < 5; ++i) {
    for (int const &num : rhs[(i + rhs_min_idx) % 5]) {
      rhs_ss << num;
    }
  }

  return lhs_ss.str() > rhs_ss.str();
}

std::ostream &operator<<(std::ostream &os, solution const &sol) {
  // find the index of the triplet with min outer number
  int sol_min_idx = 0;
  int sol_min_val = sol[0][0];

  for (int i = 1; i < 5; ++i) {
    if (sol[i][0] < sol_min_val) {
      sol_min_idx = i;
      sol_min_val = sol[i][0];
    }
  }

  for (int i = 0; i < 5; ++i) {
    for (int const &num : sol[(i + sol_min_idx) % 5]) {
      os << num;
    }
  }

  return os;
}

int main() {
  std::array<int, 10> nums{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

  std::vector<solution> solutions;
  while (std::next_permutation(nums.begin(), nums.end())) {
    if (is_valid_solution(nums)) {
      solution sol;
      for (int t = 0; t < 5; ++t) {
        sol[t] = {nums[t], nums[t + 5], nums[((t + 1) % 5)  + 5]};
      }
      solutions.emplace_back(sol);
    }
  }

  std::sort(solutions.begin(), solutions.end(), sol_cmp);
  std::cout << solutions[0] << "\n";

  return 0;
}

// 6531031914842725
