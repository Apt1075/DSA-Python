mytuple = ("arpit","sanjay","arjun","ankit","raja")
print(mytuple)


print("\n After changes = " , mytuple[1:4])

mylists = list(mytuple)
mylists[1] = "vivek"

mylists[2] = "Satyam"

print("\n After changes = " , mylists)

mytuple = tuple(mylists)

print("\n After changes = " , mytuple)



mytuple1 = ("arpit","sanjay","arjun","ankit","raja")
mytuple2 = (1,2,3,4,5,6,7,8,9)

print("concate= ", mytuple1 + mytuple2)


print("sanjay" in mytuple1)

print("sanjay" not in mytuple1)

print("min = ",min(mytuple2))

print( "max = ", max(mytuple2))

print("length = ", len(mytuple2))