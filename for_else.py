num = [11, 16, 18, 21, 21] 

for i in num:
    if i % 5 == 0:
        print(i)
        break # coz we want only first number not all COMPULSARY
    else:
        print("not found #if-else")
else: #for else prints only when for loop complited
    #where if else gets executed everytime with for loop
    #try changing num 21 to 20 and check output
    print("not found #for-else")