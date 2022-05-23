import os
import csv

csvpath= "/Users/alexanderpowers/Documents/GitHub/pythonChallenge/PyPoll/Resources/electionDataTest.csv"
total=[]
candidates=[]
candOne=[]
candTwo=[]
candThree=[]
candFour=[]


with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    # print(csvreader)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    for row in csvreader:

        if any(row[1]):
            total.append(str(row[1]))
            totalVotes = len(total)
        if str(row[2]):
            candidates.append(str(row[2]))
            candidatesSet=set(candidates)
            candTotal=int(len(candidatesSet))
            candSetList=list(candidatesSet)
            for x in range(candTotal):
                x=candidates.count(candSetList[int(candTotal)-1])

        # if str(candidatesSet) == str(row[2]):
        #     candOne.append(str(row[2]))
        #     totalCandOne=len(candOne)


print(totalVotes)
print(candidatesSet)
print(x)
    # # print(candidatesList)


