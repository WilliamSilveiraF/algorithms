use std::io;

fn main() {
    let mut dona_monica = String::new();
    io::stdin().read_line(&mut dona_monica).expect("Failed to read line");
    let dona_monica: i32 = dona_monica.trim().parse().expect("Failed to parse input as integer");
    
    let mut filho_a = String::new();
    io::stdin().read_line(&mut filho_a).expect("Failed to read line");
    let filho_a: i32 = filho_a.trim().parse().expect("Failed to parse input as integer");

    let mut filho_b = String::new();
    io::stdin().read_line(&mut filho_b).expect("Failed to read line");
    let filho_b: i32 = filho_b.trim().parse().expect("Failed to parse input as integer");

    let filho_c = dona_monica - (filho_a + filho_b);

    let max_age = filho_a.max(filho_b.max(filho_c));

    println!("{}", max_age);
}