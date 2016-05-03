# LIST
# List Extension I
Election_Results=[]
City=["Oyo", "Osun", "Ogun", "Edo", "Benin", "Abuja", "Lagos", "Abi", "Benue", "Ibadan", "Ondo"]
Vote=[21,47,58,44,21,83,101,45,64,11,14]
for i in range(11):
    print(City[i],'\t= ',Vote[i])
    Election_Results=[(City[i],Vote[i])]
print(Election_Results)

# List Extension II
election_results=[]
city=["Oyo", "Osun", "Ogun", "Edo", "Benin", "Abuja", "Lagos", "Abi", "Benue", "Ibadan", "Ondo"]
vote=[21,47,58,44,21,83,101,45,64,11,14]
for i in range(11):
    election_results.extend([(city[i],vote[i])])
print(election_results)

# Selected List Methods
city.append("Imo")
print(city)

city.extend(["Ibo", "Delta"])
print(city)

city.insert(6,"Eko")
print(city)

# Delete a certain elements or use list.clear() to delete all elements
del city[6]
print(city)
# Returns the index or position of the searched element
print(city.index("Lagos"))

# Remove and Returns the Last Value on the List
print(city.pop())

# Returns the ordering of the list in ascending form
city.sort()
print(city)

# Returns the ordering of the list in descending form
city.sort(reverse=True)
print(city)

# Nested List
city_vote=[]
vote=[21,47,58,44,21,83,101,45,64,11,14,55,82]
for i in range(13):
    city_vote.extend([[city[i],vote[i]]])
print(city_vote)
print(city_vote[:2])
print(city_vote[-1])
print(city_vote[0][0])
print(city_vote[0][1])

city_vote.append(["Delta",91])
print(city_vote)
print(city)
print(vote)

city_vote.insert(3,["Kogi", 69])
print(city_vote)

# To sort the above with a certain key or criteria. Import the module
# "Operator" and function "itemgetter".
# The following sort by vote results for each city
from operator import itemgetter
city_vote.sort(key=itemgetter(1))
print(city_vote)

city_vote.sort(key=itemgetter(1),reverse=True)
print(city_vote)

# Nested Loop
for i in city_vote:
    print(i)

# Nested Loop
for i in city_vote:
    for h in i:
        print(h)
# Nested Loop
for i in city_vote:
    for h in i:
        print(h, '\t', end='')
    print()
