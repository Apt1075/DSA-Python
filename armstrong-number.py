is_armnumber = 153
cpy_armnumber = is_armnumber
sum =0 
while is_armnumber > 0:
    last_digit = is_armnumber % 10
    # print(last_digit)
    sum = sum + last_digit ** 3
    # print(sum)
    is_armnumber = is_armnumber // 10

if sum == cpy_armnumber:
    print("Number is armstrong")
else:
    print("Number is not armstrong")