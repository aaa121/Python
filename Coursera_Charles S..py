'''
Assigning from User Input for string
'''
name=input("What is your name?")
age=input("What is your age?")
print("Hello,",
      "Thanks for the response",
      name+ " Atanda and we are glad you are",
      age+" years old")

'''
Assigning from User Input for Numeric. it is used if we don't
have values for a variable that hasn't been pre-defined. The only caveat
is that it stored the numeric as string. There is need to convert to numeric i.e. integer or float using TYPE-CASTING
programming notion. Such as int(), float(), and str(). If the variables will be used in subsequent programme. it is better
to redefine them as:
cost=int(cost)
'''
cost=input("what is the total cost of production?")
output=input("How many unit was produced?")
CPU=int(cost)/int(output)
print("The cost per unit is $ ", CPU)


'''
Calculate the Range of the Quadratic Equation Value
'''
ap=float(input("Enter the estimated positive value of X:"))
an=float(input("Enter the estimated negative value of X:"))
b=float(input("Enter the coefficient of X:"))
c=float(input("Enter the last integer in the Equation:"))
QEp=(ap**2)+(b*ap)+c
QEn=(an**2)+(b*an)+c
print("The Range of the Quadratic Equation is between", QEn, "and ", QEp)

'''
Calculate the Range of the Quadratic Equation Value. Rounded up to two decimal value
'''
ap=float(input("Enter the estimated positive value of X:"))
an=float(input("Enter the estimated negative value of X:"))
b=float(input("Enter the coefficient of X:"))
c=float(input("Enter the last integer in the Equation:"))
QEp=(ap**2)+(b*ap)+c
QEn=(an**2)+(b*an)+c
'''
The syntax %0.2f is used to round up to a certain decimal place and it must be within single
or double quotation. i.e. "%0.2f"
Also, the numeric value to be rounded up must have the percentage prefix % i.e %x if x =30
'''
print("The Range of the Quadratic Equation is between %0.2f" %QEn, "and %0.2f" %QEp)

#This computes formatting for two decimal place
a=3
b=7
c1=a/b
c=a/b
print(c1, "Rounded up to Two decimal Place", "%0.2f" %c)

#PROGRAM FOR SOLVING QUADRATIC EQUATION

#PROGRAM FOR SOLVING QUADRATIC EQUATION

# Import the complex number module
import cmath
'''
The QE should be in the format ax**2 + bx + c =0
Example 1: a = 2; b =5; c= 2
Example 2: a = 2.3; b = 1.72; c =5.02
'''
a=float(input("Enter value for a:"))
b=float(input("Enter value for b:"))
c=float(input("Enter value for c:"))
d=cmath.sqrt(b**2-(4*a*c))
QE1 = (-b-d)/(2*a)
QE2 = (-b+d)/(2*a)
print("The solution for x is either", QE1," or ", QE2)
'''
It is not possible to convert complex to float. TO round to a specific decimal place is not possible:
print("The solution for x is either %0.2f" %QE1," or %0.2f" %QE2)

The above can be represented as:
print("The solution for x is either {0} or {1}".format(QE1,QE2))
'''


# CREATE A QUADRATIC EQUATION FUNCTION
import cmath
def quadratic(a,b,c):
    '''
    quadratic(num,num,num) -> num or num
    The function evaluates  the quadratic equation given the
    parameters ax**2 + bx + c =0. It returns two possible value for x.
    >>> quadratic(2,5,2)
    (-2+0j) or (-0.5+0j)
    '''
    d=cmath.sqrt(b**2-(4*a*c))
    QE1 = (-b-d)/(2*a)
    QE2 = (-b+d)/(2*a)
    QE = "{0} or {1}".format(QE1,QE2)
    return QE


# HOW TO REQUEST FOR COMPLEX NUMBER INPUT AND CONVERT
import cmath
'''
The following program computes the sqaure root of complex number
'''
cnum=eval(input("Enter the complex number in the 0+0j:"))
csqrt=cnum**0.5
print(csqrt)
'''
Alternatively, the square root function under the complex number module can be used. Both give the same output
'''
csqrt2=cmath.sqrt(cnum)
print(csqrt2)


# DAY DIFFERENCE
def days_difference(d1,d2):
    '''
    (int, int) -> int
    :param d1: Current day
    :param d2: Future day
    :return: The difference between current and future day.

    >>> days_difference(5, 2)
    3
    '''
    return d2-d1

#WEEK DAY DIFFERENCE
def week_day_difference(d1,d2):
    '''
    (int,int) -> int
    :param d1: current weekday
    :param d2: Future day (How many days ahead from today do you want to know).
    :return: The exact day of the week from Sunday to Saturday i.e. 1 - 7

    >>> week_day_difference(1,15)
    (1, 'Sunday')
    '''
    x=(days_difference(d1,d2))%7 + 1
    day=["Undefined", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for i in range(8):
        if i is x:
            y=day[i]
    return x,y

print(week_day_difference(1,15))

#GET WEEK DAY AHEAD
def weekday_ahead(d1,d2):
    '''
    (int,int) -> int
    :param d1: current weekday
    :param d2: Future day (How many days ahead from today do you want to know?).
    :return: The exact day of the week from Sunday to Saturday i.e. 1 - 7

    >>> weekday_ahead(6,1)
    (7, 'Saturday')
    '''
    x=(d1+d2-1)%7 + 1
    day=["Undefined", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for i in range(8):
        if i is x:
            y=day[i]
    return x,y

print(weekday_ahead(6,1))


day=["Undefined", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
x=6
for i in range(8):
    if i is x:
        y=day[i]
        print(y)




#STRING: Escape Sequence
'''
\' single quote;
\" double quote;
\t tab
\n new line
\r carriage return or read all the following string. It reinforces all the escape sequence excluding \t (tab)
'''
print("I said: 'I love you Laura'. Isn\'t it?")
print("I said: 'I love you Laura'. Isn\"t it?")
print("I said: 'I love you Laura'. \nIsn\'t it?")
print("I said: \t'I love you Laura'. \nIsn\'t it?")
print("I said: \r'I love you Laura'. \nIsn\'t it?")
print("I said: \r'I love you Laura'. \rIsn\'t it?")
print("\r I said: 'I love you Laura'. Isn't it?")

print("\tUndefined", "\tSunday", "\tMonday")
print("\nUndefined", "\nSunday", "\nMonday")



#STRING OPERATIONS
dob="Monday" + " " \
               +str(1980)
print(dob)
lv="I love you Honey! " * 3
print(lv)

lvl="I love you" + " " + "Laura"
print(lvl)

lvl1=lvl+" "
print(lvl1*3)

#Multiplication of strings with negative or zero returns nothing.
lvl2=lvl1*-3
print(lvl2)

first='John'
last='Doe'
print(first+', '+last)
'''
This returns syntax error:

print(first+,', ',+last)
'''

#PRINT FORMAT
help(print)
print("\nUndefined", "\nSunday", "\nMonday", sep=",")
print("Undefined", "\tSunday", "\tMonday", sep=",")
print("Undefined", "\tSunday", "\tMonday", sep="-")
print("Undefined", "Sunday", "Monday", sep=" ", end="\n")
print("Undefined", "Sunday", "Monday", sep=" ", end="*$*\n")
print("Sunday", "Monday", sep=", ", end=". Weekdays. \n")

#LENGTH: STRING, LIST, & OPERATIONS
months=["January", "February", "March", "April"]
print(len(months))
print(len(months[0]))
print(len(months[1]))
print(len(months[1])*14)
print(len(months[2])**4)
print(len(months[0])/4)
print(len(months[3])//4)
print(len(months[2])%4)
print(len("akin")+2)


#BUILT-IN FUNCTION MAX & MIN
numlist=[3,4,2,11,23,6,87,9,3.4,99.4,21,101.999]
print(max(numlist))
print(min(numlist))
print(round(max(numlist)))


#TOP THREE STOCKS IN TERMS OF PRICE
stockprices=[62.3,45.2,8.23,88.1,79.2,34,21.2,9.3,64,3,72.2,1.3]
def top3stocks(stockprices):
    '''
    To get the top three maximum values
    >>> list(int,float) -> [num,num,num]
    :param stockprices: Integer or float or both in the list
    :return: returns top three numeric values in ascending order
    '''

    stockprices.sort()
    return stockprices[-3:]
print(top3stocks(stockprices))

day=['a','c','k','b']
day.sort()
print(day)


#BOOLEAN OPERATORS FOR STOCKS PICKING BASED ON GROWTH
#Case 1
ANX=True
BNZ=True
ANX and BNZ
ANX or BNZ
(not ANX) and BNZ
not(ANX and BNZ)
#Case II
ANX=True
BNZ=False
ANX and BNZ
ANX or BNZ
(not ANX) and BNZ
not(ANX and BNZ)
#Case III
ANX=False
BNZ=True
ANX and BNZ
ANX or BNZ
(not ANX) and BNZ
not(ANX and BNZ)
#Case IV
ANX=False
BNZ=False
ANX and BNZ
ANX or BNZ
(not ANX) and BNZ
not(ANX and BNZ)

ANX=bool(input("Enter either one or zero:"))
BNZ=True
stock=ANX+BNZ
print(stock)

print(3>1)
print(round(3.6)<=4)
print(4<2.5)
print(1 != 0)
print(pow(3,2,4)>=round(float("2.964782"),3)) #if int(2.964782) was used, it will returns syntax error.
print(True != True)
print(True != False)
print(True == False)
print((3<5) and (5 !=True))
print((3<5) and (5 !=False))

#Using Numbers and Strings with Boolean Operators
print(not 1) # Integer or Float greater or equal to 1 returns True
print(not 0)
print(not 76.2)
print(not None) #None and empty string '' return False. Otherwise True
print(not '')
print((not "Bob") and True)

print((2>3) and 1/0) #Short-Circuit operations. It first eavlautes from left and stop since the condition of and has been met.
#print((2>3) and 1/0)  will return syntax

# IN operator with Boolean
dob=str(input("Enter your date of birth in the format DD-MM-YYYY:")) #Example input 22-02-1980
print(dob)
dob2=dob + ". I was born in Jan"
print(dob2)
print('Jan' in dob2)
print('02' in dob)



#Boolean with ASCII (American Standard Code for Information Interchange)\
#Upper case letter has lower value compared to lower case value
print("D" > "d")
print("d" > "D")
print('aBc' == 'abc')
print('aBc' > 'abc')
print('aBc' <= 'abCd')
print('aBc' >= 'abCd')
print('aBc' != 'abCd')




#Confidence Interval for test of Hypothesis at 95% CI
def coverage_rate_95(zscore)

    '''
    >>> num -> num, str
    :param zscore: Input is numeric. The calculated Zscore
    :return: Numeric and Decision iff (if and only if) is within or outside the interval

    Examnples:
    >>> coverage_rate_95(1.23)
    1.23  is within the coverage range. Reject Null Hypothesis.

    >>> coverage_rate_95(-2.13)
    -2.13  is not within the coverage range. Accept Null Hypothesis.
    '''
    x= -1.96 <= zscore <= 1.96
    if x == True:
        print(zscore, " is within the coverage range. Reject Null Hypothesis.")
    else:
        print(zscore, " is not within the coverage range. Accept Null Hypothesis.")
    return
coverage_rate_95(1.23)
coverage_rate_95(-2.13)
help(coverage_rate_95)

# NESTED IF Statement for Confusion Matrix
predicted=int(input("Enter the Predicted Signal Occurence, either True (1) or False (0):"))
actual=int(input("Enter the Actual Signal Occurence, either True (1) or False (0):"))
if predicted ==1:
    if actual == 1:
        print("True Positive")
    else:
        print("False Positive")
elif predicted == 0:
    if actual == 0:
        print("True Negative")
    else:
        print("False Negative")
else:
    print("Wrong Input value. Enter either 1 or 0")

#Confusion matrix II
predicted=int(input("Enter the Predicted Signal Occurence, either True (1) or False (0):"))
actual=int(input("Enter the Actual Signal Occurence, either True (1) or False (0):"))
if predicted ==True:
    if actual == True:
        print("True Positive")
    else:
        print("False Positive")
elif predicted == False:
    if actual == False:
        print("True Negative")
    else:
        print("False Negative")
else:
    print("Wrong Input value. Enter either 1 or 0")


#Math Module
import confidence_interval
ci95=confidence_interval.coverage_rate_95(2.2)
print(ci95)

import math
par1=math.sqrt(4)
print(par1)

from math import sqrt, pi, log10
par2=log10(4)
print(par2)

from math import *
par3=pow(2,4)
print(par3)

dir(__builtins__)
help(__builtins__)




