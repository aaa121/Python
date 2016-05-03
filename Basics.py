print('I love myself')
print('Have been looking for you over six months')
user=[2,3,45,18,7,8,98]
Name = ["ade", "funke", "segun", "Ayo"]
print(user)
print('what exACTLY IS HAPPENING')
if user[-3] is 18:
    print('The user is an Adult and 18 years old')
elif user[3] < 18:
    print('The user is a teenager and less than 18 years old')
elif user[3] <26:
    print('The user is an adult but less 25 years of age')
else:
    print('The user is a teenager and older than 25')

for x in user:
    print(x)
for y in Name:
    print(y)
    print(len(y))
for h in range(0,101,10):
    print(h)
for g in range(5):
    print('University of Canterbury')
while user[1] < 18:
    print(user[1])
    user[1]+=1

#How to print number and string together i.e concantenating strings
print(user[2], Name[1])
'''
The three quote above and below is for multi-line comments
'''
jackport=18
for x in range(0,101,1):
        if x is jackport:
            print(x," is the Lucky Number!")
            break
        else:
            print(x)

for x in range(101):
    if x%4 is 2:
        print(x)
'''
The following code generate the same number with multiple of 4
for x in range(0,101,4):
    print(x)
'''
for x in range(0,50,1):
    if x in user:
        continue
        #Ensure the statement after continue or  break is indented with the if or for statement
    print(x)







