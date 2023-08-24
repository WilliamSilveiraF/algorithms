use std::io;
use std::str::FromStr;

fn main() {
    
    let timing = read_input();
    let speed_avarage = read_input();


    let fuelNedded: f64 = (timing as f64 * speed_avarage as f64) / 12.0;
    println!("{:.3}", fuelNedded);
}

fn read_input() -> i64 {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    input.trim().parse().expect("Failed to read line as integer")
}