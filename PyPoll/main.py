import os
import csv

csvpath= "/Users/alexanderpowers/Documents/GitHub/pythonChallenge/PyPoll/Resources/election_data.csv"

candidates=[]
totalVotes=0
votes={}
percent={}
candString={}
candStringList=[]

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        totalVotes = totalVotes + 1
        candidateName = row[2]

        if candidateName not in candidates:
            candidates.append(candidateName)
            votes[candidateName] = 0
        votes[candidateName] = votes[candidateName] + 1
        percent[candidateName] = (votes[candidateName] / totalVotes) * 100
        candString[candidateName] = (f"{candidateName}: {int(percent[candidateName])}% ({votes[candidateName]})")
        candStringList=candString.values()

textFile= open(r"/Users/alexanderpowers/Documents/GitHub/pythonChallenge/PyPoll/Analysis/analysis.txt", "w" )

str1=("Election Results")
str2=("-------------------------")
str3=(f"Total Vote: {totalVotes}")
str4=("-------------------------")
strP='\n'.join(candStringList)
str5=("-------------------------")
winner=max(votes,key=votes.get)
str6=(f"Winner: {winner}")
str7=("-------------------------")

textL=[str1,str2,str3,str4,strP,str5,str6,str7]
textFinal='\n'.join(textL)
print(textFinal)

textFile.writelines(textFinal)




