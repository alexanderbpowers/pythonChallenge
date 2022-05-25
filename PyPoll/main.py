import os
import csv

csvpath= "/Users/alexanderpowers/Documents/GitHub/pythonChallenge/PyPoll/Resources/election_data.csv"

total=[]
candidates=[]



with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)



    for row in csvreader:

        if any(row[1]):
            total.append(str(row[1]))
            totalVotes = len(total)
        if str(row[2]):
            candidates.append(str(row[2]))
            candidatesSet=set(candidates)
            candSetList=list(candidatesSet)
        CandVotesAmount = {}
        CandVotesPercent = {}
        CandString = []
print("hello")
        for name in candidates:
            CandVotesAmount[name]=candidates.count(name)
            CandVotesPercent[name]=(CandVotesAmount[name]/totalVotes)*100
        for name in candidatesSet:
            CandString.append(f"{name}: {int(CandVotesPercent[name])}% ({CandVotesAmount[name]})")


print("finished looping")
textFile= open(r"/Users/alexanderpowers/Documents/GitHub/pythonChallenge/PyPoll/Analysis/analysis.txt", "w" )

str1=("Election Results")
str2=("-------------------------")
str3=(f"Total Vote: {totalVotes}")
str4=("-------------------------")
strP='\n'.join(CandString)
str5=("-------------------------")
winner=max(CandVotesAmount,key=CandVotesAmount.get)
str6=(f"Winner: {winner}")
str7=("-------------------------")

textL=[str1,str2,str3,str4,strP,str5,str6,str7]
textFinal='\n'.join(textL)
print(textFinal)

textFile.writelines(textFinal)




