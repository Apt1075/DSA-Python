number = 5847
reverse = 0
while number > 0:
    last_digit  = number %10
    print(last_digit)
    reverse = reverse * 10 + last_digit
    number = number // 10
print(reverse)

