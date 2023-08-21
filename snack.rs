use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let values: Vec<f64> = input
        .trim()
        .split_whitespace()
        .map(|s| s.parse().expect("Parse error"))
        .collect();

    let a = values[0] as i32;
    let b = values[1];

    let price = match a {
        1 => 4.00,
        2 => 4.50,
        3 => 5.00,
        4 => 2.00,
        5 => 1.50,
        _ => 0.00, // default case
    };

    println!("Total: R$ {:.2}", price * b);
}