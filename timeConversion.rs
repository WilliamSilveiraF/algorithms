use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let mut time = input.trim().parse().expect("Failed to parse input as integer");

    let hours: i32 = time / 3600;
    time = time - (hours * 3600);
    let minutes: i32 = time / 60;
    time = time - (minutes * 60);
    let seconds: i32 = time;

    println!("{}:{}:{}", hours, minutes, seconds);
}