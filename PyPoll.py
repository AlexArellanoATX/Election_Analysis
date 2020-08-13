#Module2_Exercise deliverables: PseudoCode
#•	Total number of votes cast
#•	A complete list of candidates who received votes
#•	Total number of votes each candidate received
#•	Percentage of votes each candidate won
#•	The winner of the election based on popular vote

#Add dependencies for analyzing CSV files
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a variable to count total votes
total_votes = 0
#Declare list for Candidate names
candidate_options = []
#Declare an empty dictionary to tally votes by candidate
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)

    #Print each row in CSV file
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        #If statement, add name if not in candidate options list already
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #Begin tracking candidates' vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        #Save results to a text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    print(election_results, end="")
    #Save final vote count to text file
    txt_file.write(election_results)

    #Loop thru candidate_votes to find % of votes for each candidate
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        # print out each candidate's name, vote count, and percentage of votes to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to text file
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        #Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            #Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    # print out the winning candidate, vote count and percentage to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)