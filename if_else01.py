#find user is under age or 18+.
print("Enter user age:- ")
age = input()
user_age = int(age)
if user_age <= 18:
    print("User age is", user_age, "User is under age.")
else:
    print("User age is", user_age, "User is 18+.")