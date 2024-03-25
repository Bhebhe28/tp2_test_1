"""2.1 Write a python function named “register_party” that takes a list of parties. Each party 
must be presented by key value pairs. The keys should be “party_name”, “reg_number”, 
“member_count”). The function should check if the new party has acceptable number of 
members for it to be registered as per the requirements narrated in the scenario. Note: this 
function must be written under the git branch that you created in question 1.4 above. """

def register_party(parties):
    for party in parties:
        party_name = party.get("party_name")
        reg_number = party.get("reg_number")
        member_count = party.get("member_count")
        
        # Check if the party has an acceptable number of members
        if member_count >= 5000:
            print(f"The party '{party_name}' with registration number {reg_number} has an acceptable number of members.")
        else:
            print(f"The party '{party_name}' with registration number {reg_number} does not have enough members for registration.")


parties = [
    {"party_name": "Party A", "reg_number": 100001, "member_count": 4800},
    {"party_name": "Party B", "reg_number": 100002, "member_count": 5200},
    {"party_name": "Party C", "reg_number": 100003, "member_count": 5300}
]
register_party(parties)

"""2.2 Now a new party called MK party which has 5300 members wants to apply to register the 
party for the next election. Write python statements that will show how will the function that
you created in question 2.1 be executed such that it registers the MK party if it meets the 
criteria as per IEC regulations. Assume that the last party that was registered had a registration 
number 10003318, and every new party that is being registered will be generated a registration 
number that increments the last registered party by 1"""
# Assuming the last registered party had registration number 10003318
last_registration_number = 10003318
new_registration_number = last_registration_number + 1

# New party details
mk_party = {"party_name": "MK Party", "reg_number": new_registration_number, "member_count": 5300}

# Execute the function for the MK party
register_party([mk_party])

""" 2.3 Implement a function called “update_voter_info” where each key is a voter_id and the 
value is another dictionary containing name, voting_district and has_voted. The function 
should update the voter’s information or add a vote if not already voted. Very important hint:
you should think of best practices for source code management and collaboration using git, 
for instances; is it a good practice to answer this question under the directories that are already 
existing or you should create a feature branch for development. From this question onwards 
you won’t be guided like you have been on questions prior to this. Always think best practices 
for software development as discussed in class. Create a new file, new directory, new feature 
branch where necessary."""

def update_voter_info(voter_info, voter_id, name, voting_district, has_voted):
    # Check if the voter is already in the database
    if voter_id in voter_info:
        # Update the voter's information
        voter_info[voter_id]["name"] = name
        voter_info[voter_id]["voting_district"] = voting_district
        voter_info[voter_id]["has_voted"] = has_voted
        print(f"Voter with ID {voter_id} updated successfully.")
    else:
        # Add the voter to the database
        voter_info[voter_id] = {"name": name, "voting_district": voting_district, "has_voted": has_voted}
        print(f"New voter with ID {voter_id} added to the database.")


voter_info = {
    "1234": {"name": "John Doe", "voting_district": "District A", "has_voted": False},
    "5678": {"name": "Jane Smith", "voting_district": "District B", "has_voted": True}
}

# Update voter information or add new voter
update_voter_info(voter_info, "9012", "Alice Johnson", "District C", False)


"""2.4 Using list comprehension and the filter function, write a piece of code that filters out all 
parties from a given list that have less than 1,000 members. Use ALL the parties that are on 
the ballot paper in Annexure A as your list elements, only capture their abbreviation as 
elements e.g. capture EFF on your list of elements instead of “Economic Freedom Fighters”
as it is displayed using EFF abbreviation on the ballot paper"""


parties = ["ANC", "DA", "EFF", "IFP", "ACDP"]  # Assuming these are the parties with their abbreviations
filtered_parties = [party for party in parties if len(party) >= 1000]
print(filtered_parties)


"""2.5 Rewrite the list comprehension in question 2.4 into a normal list data structure."""
filtered_parties = []
for party in parties:
    if len(party) >= 1000:
        filtered_parties.append(party)
print(filtered_parties)

"""2.6 Write a python expression using a lambda function and the filter function to extract only 
those records where the voter is marked as registered ('registered': True). Assign the result 
to a variable named “registered_voters”."""

voters = [
    {"id": 1, "name": "Alice", "registered": True},
    {"id": 2, "name": "Bob", "registered": False},
    {"id": 3, "name": "Charlie", "registered": True}
]

registered_voters = list(filter(lambda x: x["registered"], voters))
print(registered_voters)
