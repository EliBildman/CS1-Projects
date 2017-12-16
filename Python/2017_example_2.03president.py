age = int(input("Age: "))
residency = int(input("Years as resident of US: "))
natural = input("Are you a natural born citizen(y/n): ")
print(age > 35 and residency >= 14 and natural == "y")
