use std::io::prelude::*;
use std::fs::File;

fn main(){
  let input_file = "input_file";
  let input_captcha = read_file(input_file);
  //println!("Checked: {}",check_if_match(1,1));
  let mut sum = 0;
  println!("Array:{}",decompose_string(input_captcha));
}

fn read_file(filename: &str) -> String {
  let mut f = File::open(filename).expect("File not found");

  let mut input_captcha = String::new();
  f.read_to_string(&mut input_captcha)
    .expect("Couldn't read file");

  //println!("With text:\n{}", input_captcha);
  input_captcha
}

fn decompose_string(input_string: &str) -> &'input_captcha str {
  let first_character = &input_string[0..1];
  let remaining_characters = &input_string[1..];
  first_character
}

fn check_if_match(a: i32, b: i32) -> i32 {
  let ret = 
    if a == b {
      a
    } else {
      0
    };
  ret
}
