num = 123
cpy_num = num
reverse = 0
while num > 0:
    last_digit = num %10
    reverse = reverse * 10 + last_digit
    num  = num // 10

if reverse == cpy_num:
    print("Number is palindrome")
else:
    print("Number is not palindrome")

