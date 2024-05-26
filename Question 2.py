def binary_to_decimal(binary_str):
  if not all(char in '01' for char in binary_str):
    return None
  digits = list(binary_str)[::-1]
  decimal_value = 0
  for i, digit in enumerate(digits):
    if digit == '1':
      decimal_value += 2**i

  return decimal_value
while True:
  binary_str = input("Enter a binary number : ")
  decimal_value = binary_to_decimal(binary_str)

  if decimal_value is not None:
    print(f"The decimal equivalent of {binary_str} is {decimal_value}.")
    break
  else:
    print("Invalid binary input. Please try again.")