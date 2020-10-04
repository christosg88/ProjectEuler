fn main() {
  let mut first = 1;
  let mut second = 1;
  let mut evens_sum = 0;

  while second <= 4_000_000 {
    let sum = first + second;
    if sum % 2 ==  0 {
      evens_sum += sum;
    }

    second = first;
    first = sum;
  }

  println!("{}", evens_sum);
}
