use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let n: i32 = input.trim().parse().expect("Failed to parse input as integer");

    for idx in 1..11 {
        println!("{} x {} = {}", idx, n, idx * n);
    }
}