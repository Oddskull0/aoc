from utils import read_file_as_string_list

def get_digits(input: str) -> int:
  first_digit=None
  second_digit=None
  len_input = len(input)
  digits=['0','1','2','3','4','5','6','7','8','9']
  for i in range(len_input):
     c = input[i]
     if c in digits:
        first_digit=c
     if first_digit is not None:
        break
     
  for i in range(len_input):
     j = len_input - i - 1
     c = input[j]
     if c in digits:
        second_digit=c
     if second_digit is not None:
        break
  if second_digit is None:
     second_digit = first_digit

  return int(first_digit + second_digit)

def part1():
    test_input =["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    real_input = read_file_as_string_list("1.txt")
    print(sum(list(map(get_digits, real_input))))

part1()