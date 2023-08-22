use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let distance: f64 = input.trim().parse().expect("Failed to parse input as integer");

    let mut input2 = String::new();
    io::stdin().read_line(&mut input2).expect("Failed to read line");
    let fuel: f64 = input2.trim().parse().expect("failed to parse input2 as float64");

    let result = distance as f64 / fuel;
    println!("{:.3} km/l", result);
}