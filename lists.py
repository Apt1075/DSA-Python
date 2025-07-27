demo = ["Arpit","Sanjay","arjun","ankit","raja"]

print(demo)

demo[4] = "vikash"

print("updated lists = ",demo)


del demo[0] #del keywords specfic for keys
print("after deletion lists = ", demo)


del demo[1:2] #del keywords specfic for keys
print("after deletion from 1 to 2 lists = ", demo)

demo.remove("vikash") #remove keywords for value if exits
print("after remove the lists = ", demo)