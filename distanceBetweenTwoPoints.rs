use std::io;
use std::f64;

fn square(number: f64) -> f64 {
    number * number
}

fn main() {
    let (mut x1, mut y1, mut x2, mut y2): (f64, f64, f64, f64);
    let (diff_de_x_quad, diff_de_y_quad, res): (f64, f64, f64);

    let input1 = read_input();
    x1 = input1.0;
    y1 = input1.1;

    let input2 = read_input();
    x2 = input2.0;
    y2 = input2.1;

    diff_de_x_quad = square(x2 - x1);
    diff_de_y_quad = square(y2 - y1);

    res = f64::sqrt(diff_de_x_quad + diff_de_y_quad);
    println!("{:.4}", res);
}

fn read_input() -> (f64, f64) {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");

    let mut iter = input.split_whitespace();
    let a: f64 = iter.next().unwrap().parse().expect("Expected a float");
    let b: f64 = iter.next().unwrap().parse().expect("Expected a float");

    (a, b)
}