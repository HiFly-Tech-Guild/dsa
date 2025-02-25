use std::io;

fn gcd(mut a:i32, mut b:i32)->i32{
    while b!=0{
        let r:i32 = a%b;
        a=b;
        b=r;
    }
    return a;
}

fn main(){
    let a:i32;
    let b:i32;
    let mut buffer:String = String::new();
    println!("Enter first number:");
    io::stdin().read_line(&mut buffer).expect("failed to reed user input");
    a = match buffer.trim().parse(){
        Ok(num) => num,
        Err(_) => {
            println!("Error parsing string");
            return;
        }
    };
    buffer = String::new();
    println!("Enter second number:");
    io::stdin().read_line(&mut buffer).expect("failed to reed user input");
    b = match buffer.trim().parse(){
        Ok(num) => num,
        Err(_) => {
            println!("Error parsing string");
            return;
        }
    };
    let ans = gcd(a,b);
    println!("GCD(a,b)={}",ans);
}