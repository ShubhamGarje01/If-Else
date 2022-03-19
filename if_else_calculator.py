#create a terminal operator based calculator using python
print("\t### CALCULTOR ###")
print("enter 1st number:- ")
n1 = input()
print("enter 2nd number:- ")
n2 = input()
print("Choose Operation\n")
print("1.Addition")
print("2.Substaction")
print("3.Multiplication")
print("4.Division")

choice = input()
if int(choice) == 1:
    print("You Choose Addition\n")
    ans = int(n1) + int(n2)
    print("Addition of ",n1, "and", n2, "is:-->", ans)

elif int(choice) == 2:
    print("You Choose Substaction\n")
    ans = int(n1) - int(n2)
    print("Substraction of ",n1, "and", n2, "is:-->", ans)

elif int(choice) == 3:
    print("You Choose Multiplication\n")
    ans = int(n1) * int(n2)
    print("Multiplication of ",n1, "and", n2, "is:-->", ans)

elif int(choice) == 4:
    print("You Choose Division\n")
    ans = float(n1) / float(n2)
    print("Division of ",n1, "and", n2, "is:-->", ans)
else:
    print("Wrong Choice Buddy")

