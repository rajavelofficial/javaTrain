# online_voting.py

voter = input("Enter voter name: ")

age = int(input("Enter voter age: "))

candidate = input("Enter candidate name: ")

print("Voter Name:", voter)
print("Candidate Selected:", candidate)

if age >= 18:
    print("Eligible to Vote")
    vote_status = "Vote Accepted"
else:
    print("Not Eligible to Vote")
    vote_status = "Vote Rejected"

print("Vote Status:", vote_status)

voter_id = input("Enter voter ID: ")

print("Voter ID:", voter_id)

for i in range(3):
    print("Voting Process Completed")

print("Online Voting System")
print("Thank You")