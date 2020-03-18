age = 15

if age < 5:
    print("stay home")
elif (age >=5) and (age <=6):
    print("Go to kindergarten")
elif (age > 6) and (age <= 17):
    print("Grade", (age - 5))
else:
    print("College")


# condition_true if condition else condition_false
canVote = True if age >= 18 else False
print(canVote)
