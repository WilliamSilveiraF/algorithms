use std::io;

fn main() {
    let gradeA = read_input();
    let gradeB = read_input();
    let gradeC = read_input();

    let avarage = (gradeA * 2.0 + gradeB * 3.0 + gradeC * 5.0) / 10.0;

    println!("MEDIA = {:.1}", avarage);
}

fn read_input() -> f64 {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    input.trim().parse().expect("Failed to read line as float64")
}