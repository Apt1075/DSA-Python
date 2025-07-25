name = 'mayank rawat'
count_srting = {}
for char in name:
    if char in count_srting:
        count_srting[char] +=1
    else:
        count_srting[char] = 1
print(count_srting)
