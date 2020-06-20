# Add dependencies.
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

# County list
county_list =[]
# Declare the empty dictionary for votes cast in each county in the election 
county_votes_dict = {}
# County with most votes and Count tracker
top_county = ""
top_county_count = 0
top_county_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1
        # candidate name from each row
        candidate_name = row[2]
        # county name from each row
        county_name = row[1]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Initialize that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # If the county does not match any existing counties...
        if county_name not in county_list:
            # add county to the list of counties
            county_list.append(county_name)
            # Initialize that county's votes count
            county_votes_dict[county_name] = 0
        # Add a vote to that county's votes
        county_votes_dict[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes: \n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # write county section:
    for county in county_votes_dict:
        # Retrieve vote count and percentage.
        votes = county_votes_dict[county]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each county's voter count and percentage to the terminal.
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)
        # Determine top vote count, top percentage, and top county.
        if (votes > top_county_count) and (vote_percentage > top_county_percentage):
            top_county_count = votes
            top_county = county
            top_county_percentage = vote_percentage
    # Print the top county's results to the terminal.
    top_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {top_county}\n"
        f"-------------------------\n")
    print(top_county_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(top_county_summary)

    # write candidate section:
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
