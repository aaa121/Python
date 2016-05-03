user=[2,3,45,18,7,8,98]
for x in range(0,100,1):
    if x in user:
        continue
    print(x)

for x in range(101):
    if x%4 is 3:
        print(x)

ade=(2*3/4)+7
print(ade)


user=[2,3,45,18]
Name = ["ade", "funke", "segun", "Ayo"]
for x in range(4):
    print(user[x]
          ,Name[x])

while user[-3] < 20:
    print(user[-3])
    user[-3] *=2

uc=abs(round(-30.8))
print(uc)

def square(a,b):
    key=(a*b/4.5)**3
    '''
    This function performs a tricky computation
    '''
    return key

def square_root(a):
    key=a**2
    return key

deh = square_root(3)
print('deh =', deh)


ade=square(3,5)
print(round(ade))

print(ade==uc)

print(ade!=uc)

funke=True+1
print(funke)

import math
print(math.pi)


seh=3j+3+2.3j
print(seh)
print(type(seh))

my_name='Akinwsnde Atanda'
print(my_name)

saw=user.append(3)
print(saw)

def Take_home(hours, tax):
    monthly_pay=4*hours*15.10
    tax_deduct=monthly_pay*(tax/100)
    Net_pay=monthly_pay-tax_deduct
    return Net_pay
Wande=Take_home(20,16.5)
print('$',Wande)

import statistics
statistics.mean(user)

statistics.median(user)

statistics.median_low(user)

statistics.pstdev(user)



