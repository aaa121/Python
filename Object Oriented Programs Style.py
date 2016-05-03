# Two Methods can be combined
print("MoNDay".lower().capitalize())
print("Pineapple".find('p'))
fruit="pineapple"
print(fruit.find('p',fruit.count('p')))
print("monday".swapcase().capitalize())
#Format for Name and Age
Akin = 27
Funke = 28
Jummy = 29
name_age="Akin \t={}\nFunke \t={}\nJummy \t={}".format(Akin,Funke,Jummy)
print(name_age)
Election_Results=[]
City=["Oyo", "Osun", "Ogun", "Edo", "Benin", "Abuja", "Lagos", "Abi", "Benue", "Ibadan", "Ondo"]
Vote=[21,47,58,44,21,83,101,45,64,11]
for i in range(11):
    print(City[i],Vote[i])


