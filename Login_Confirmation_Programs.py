# WHILE LOOP or CONDITIONAL LOOP
i=0           # This the start value
while i < 11: # Condition: Do the loop if TRUE else stop when FALSE
    print(i)  # Execute this if the condition is TRUE
    i +=1     # Counter

h=10
while h > 0:
    print(h)
    h -=1
'''
#Infinite Loop
h=1
while h != 0:
    print(h)
    h +=1
'''
# Location Confirmation
city2=["Oyo", "Osun", "Ogun", "Edo", "Benin", "Abuja", "Lagos", "Abi", "Benue", "Ibadan", "Ondo"]
city="Lagos"
for i in city:
    name=input("Enter your name:")
    city_input=input("Enter your location or quit to exit the program:")
    while city_input != "quit":
        if city_input == i:
            print(name+"!!!\n",
                  "Than you for your interest to complete this survey ",
                  '\n about '+i,' Community Youth Development.')
        else:
            print("Ooh Ooh!!!","\nWhoops! ",name+", there is no survey for "+city_input+"\n",
                  "Thanks for your interest and Check back later.\n",
                  "... existing the program")
        print()
        print()
# Location Confirmation II
city=["Oyo", "Osun", "Ogun", "Edo", "Benin", "Abuja", "Lagos", "Abi", "Benue", "Ibadan", "Ondo"]
city2="Lagos"
input=input("Enter:")
for i in city:
    if input==i:
        print(i+" is here")
        break
    while input != i:
        continue
        print(input+" Not here")

# Location Confirmation III
city=["Oyo", "Osun", "Ogun", "Edo", "Benin", "Abuja", "Lagos", "Abi", "Benue", "Ibadan", "Ondo"]
city2="Lagos"
name=input("Enter your name:")
city_input=input("Enter your location or quit to exit the program:")
for i in range(len(city)):
    if city_input == city[i]:
        print(name+"!!!\n",
              "Thank you for your interest to complete this survey ",
              '\n about '+city[i],' Community Youth Development.')
        break
'''
    elif city_input != city[i]:
        print("Ooh Ooh!!!","\nWhoops! ",name+", there is no survey for "+city_input+"\n",
                  "Thanks for your interest and Check back later.\n",
                  "... existing the program")

    print()
    print()
'''
# location Confirmation IV
city=["Oyo", "Osun", "Ogun", "Edo", "Benin", "Abuja", "Lagos", "Abi", "Benue", "Ibadan", "Ondo"]
city2="Lagos"
input=input("Enter:")

for i in city:
    while i == input:
        print(input,"True")
        break



# While loop
i=0
while i<4:
    print(i)
    i+=1

# How to Identify the Number of Digits in certain string
password="The8t9k2"
numeric=0
sum_of_digit=0
for i in range(len(password)):
    while password[i].isdigit():
        numeric +=1
        print(numeric)
        sum_of_digit=sum_of_digit + int(password[i])
        break
print(numeric)
print(sum_of_digit)

# How to Identify the Number of Digits in certain string II
password="The8t9k2"
numeric=0
sum_of_digit=0
for i in range(len(password)):
    while password[i].isdigit():
        numeric +=1
        break
print(numeric)
'''
If the login expectation is to ensure the password contain at least two numeric digits
'''
if numeric >= 2:
    print("Valid Password Format. Click Next")
else:
    print("Password must contain at least two numeric character between 0 and 9")

# How to Identify the Number of Alphabet in certain string III
password="The8t9k2"
alphabet=0
sum_of_alphabet=0
for i in range(len(password)):
    while password[i].isalpha():
        alphabet +=1
        break
print(alphabet)
'''
If the login expectation is to ensure the password contain at least two alphabet digits
'''
if alphabet >= 2:
    print("Valid Password Format. Click Next")
else:
    print("Password must contain at least two alphabet character between a and z")


# How to Identify if the first Letter of the String is Upper case IV
password="The8t9k2"
capital=0
for i in range(1):
    while password[i].isupper():
        capital +=1 # If TRUE, 0 +1. Otherwise, it will be zero since the iteration will only execute once.
        break
print(capital)
'''
If the login expectation is to ensure the password contain at capital letter as the first character
'''
if capital is 1:
    print("Valid Password Format. Click Next")
else:
    print("The first letter of the Password must be Upper Case")





