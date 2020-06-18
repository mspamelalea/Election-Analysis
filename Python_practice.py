#print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
#    print(counties[1])
#if counties[3] != 'Jefferson'

 #  print(counties[2])

#counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not the list of counties.")

#if "Arapahoe" in counties and "El Paso" in counties:
#    print("Arapahoe and El Paso are in the list of counties.")
#else:
#    print("Arapahoe or El Paso is not in the list of counties.")

#if "Arapahoe" in counties or "El Paso" in counties:
#    print("Arapahoe or El Paso is in the list of counties.")
#else:
#    print("Arapahoe and El Paso are not in the list of counties.")

#if "Arapahoe" in counties and "El Paso" not in counties:
#   print("Only Arapahoe is in the list of counties.")
#else:
#    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

#for county in counties:
#    print(county)

#numbers = [0, 1, 2, 3, 4]
#for num in numbers:
#    print(num)

#for num in range(5):
#    print(num)

#for i in range(len(counties)):
#    print(counties[i])

counties_tuple = ("Arapahoe","Denver","Jefferson")
 
#for i in range(len(counties_tuple)):
#      print(counties_tuple[i])
#for county in counties_tuple:
#      print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#print dictionary keys
#for county in counties_dict:
#    print(county)
#alternative with keys() method
#for county in counties_dict.keys():
#    print(county)
#variable name doesn't matter
#for i in counties_dict.keys():
#    print(i)
#for i in counties_dict.values():
#    print(i)
# this does not return counties
#for county in counties_dict:
#    print(counties_dict[county])

#these two return the same; keys and values
#The first variable declared in the for loop is assigned to the keys.
#The second variable is assigned to the values.
#for county, voters in counties_dict.items():
#    print(county, voters)
#for i,j in counties_dict.items():
#    print(i,j)

for i,j in counties_dict.items():
#    print(str(i) + " county has " + str(j) + " registerd voters." )
    print(f"{i} county has {j:,} registered voters.")

#print list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
#    print(county_dict)

#returns indexes
#for county in range(len(voting_data)):
#     print(county)
#
#for county_dict in voting_data:
#    for value in county_dict.values():
#        print(value)
#the number of registered voters from each dictionary
for county_dict in voting_data:
    print(county_dict['registered_voters'])
#the counties from each dictionary
for county_dict in voting_data:
    print(county_dict['county'])
for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,}")

