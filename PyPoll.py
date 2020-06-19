# Print total votes.
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options list
candidate_options = []

# Declare the empty dictionary for votes per candidate.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1
        
        candidate_name = row[2]
        #Add the candidate name to the candidate list
        #candidate_options.append(candidate_name)
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Initialize that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Print the candidate vote dictionary.
#print(candidate_votes)
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    vote_percentage = int(votes) / int(total_votes) * 100
    #print(f"{candidate}: recieved {vote_percentage:,.1f}% of the vote.") 
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

    #Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate 
winning_candidate_summary = (
f"-------------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"-------------------------\n")
print(winning_candidate_summary)

#  Print the total votes.
#print(total_votes)

#Print the candidate list
#print(candidate_options)