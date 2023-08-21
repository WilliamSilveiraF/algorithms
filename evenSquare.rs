use std::io;

fn square(number: i32) -> i32 {
    return number * number
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let n: i32 = input.trim().parse().expect("Failed to parse input as integer");

    for idx in 1..n+1 {
        if (idx % 2 == 0) {
            println!("{}^2 = {}", idx, square(idx))
        }
    }
}