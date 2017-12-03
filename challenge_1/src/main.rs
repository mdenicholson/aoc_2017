use std::io::prelude::*;
use std::fs::File;

fn main(){
  let input_file = "input_file_2";
  let input_captcha = read_file(input_file);
  let mut input_captcha_chars: Vec<char> = input_captcha.chars().collect();
  //let s: String = input_captcha_chars.into_iter().collect();
  //println!("{}", s) ;

  let mut i = 0u32;
  loop {
    let mut i_usize = i as usize;
    println!("Char, i: {}, {}",input_captcha_chars[i_usize].to_string(), i.to_string());
    i+=1;
    println!("i {}",i);
    if i > 4 {
      break
    }
  }
  
  println!("Output of decompose:{}",decompose_to_sum(0,0,input_captcha_chars).to_string());
}

fn read_file(filename: &str) -> String {
  let mut f = File::open(filename).expect("File not found");

  let mut input_captcha = String::new();
  f.read_to_string(&mut input_captcha)
    .expect("Couldn't read file");
  //println!("With text:\n{}", input_captcha);
  input_captcha
}

fn decompose_to_sum(sum_so_far: i32, position: usize, full_array: Vec<char>) -> i32{
  let test_arr: String = full_array[..].into_iter().collect();
  let pos_i32 = full_array[position] as i32;
  println!("Pos: {}, Arrayout: {}",position.to_string(), pos_i32.to_string());
  let mut new_sum: i32 = 0;
  if position < full_array.len() -1 { 
    let addition_this_round = 
      if full_array[position] == full_array[position+1] {
        full_array[position] as i32
      } else {
        0
      };
    println!("Current addition: {}",addition_this_round.to_string());
    new_sum = addition_this_round + 
      decompose_to_sum(sum_so_far, position + 1, full_array);
  } else {
    new_sum = sum_so_far;
  }
  new_sum
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
