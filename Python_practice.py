counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
     print("El Paso is in the list of counties.")
else:
   print("El Paso is not in the list of counties.")
   
#Loops counties is already defined above county is now every item inside counties and this will print 
#everythuing inside counties 
for county in counties:
    print(county)
    
counties_tuple = ("Arapahoe", "Denver", "Jefferson")    
for i in range(len(counties_tuple)):
    print(counties_tuple[i])

# to print each dictionart in votin_data
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#retieve vauleu from each dictionary in the list of dictionaries    
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
 
#get values for each dictionary        
for county_dict in voting_data:
    print(county_dict["registered_voters"])

#get county name for each dictionary    
for county_dict in voting_data:
    print(county_dict['county'])

#F-strings
for county, voters in county_dict.items():
    print(f"{county} has {voters} registered voters")

#Multiple f-strings
# candidate_votes = int(input("How many votes did the candidate get in the election?"))
# total_votes = int(input("What is the total number of votes in the election?"))
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes." 
#     f" The total number of votes in the election was {total_votes:,}."
#     f" You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
#                {"county":"Denver", "registered_voters": 463353}, 
#                {"county":"Jefferson", "registered_voters": 432438}]
# message_output = (
#     f"{county_dict[county]} county has {voting_data[]}, registered voters.")
    
# print(message_output)
    
