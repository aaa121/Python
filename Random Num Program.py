import random as rd
# Mersenne Twister core generator:
#  GAUSSIAN RANDOM NUMBER
rd.seed(1980)
for i in range(10):
    print(rd.gauss(0,0.025))
# This is to generate a single Random Number
print(rd.random())

# Generate Uniform Random Number
print(rd.uniform(0,1))


