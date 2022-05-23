import os
import csv

csvpath= "/Users/alexanderpowers/Documents/GitHub/pythonChallenge/PyBank/Resources/budget_data.csv"
total=[]
months=[]



with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    # print(csvreader)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    for row in csvreader:


        if any(row[1]):
            total.append(int(row[1]))
            totalSum=sum(total)
            maxV=max(total)
            minV=min(total)
            if maxV==int(row[1]):
                maxM=str(row[0])
            if minV==int(row[1]):
                minM=str(row[0])
        if any(row[0]):
            months.append(str(row[0]))
            mCount= len(months)
# print(maxV)
# print(maxM)
average=totalSum/mCount

textFile= open(r"/Users/alexanderpowers/Documents/GitHub/pythonChallenge/PyBank/Analysis/analysis.txt", "w")

str1=("Financial Analysis")
str2=("----------------------------")
str3=(f"Total Monts: {mCount}")
str4=(f"Total: ${totalSum}")
str5=(f"Average Change: ${int(average)}")
str6=(f"Greatest Increase in Profits: {maxM} {maxV}")
str7=(f"Greatest Decrease in Profits: {minM} {minV}")

textL=[str1,str2,str3,str4,str5,str6,str7]
textFinal='\n'.join(textL)
print(textFinal)
# print(str1)
# print(str2)
# print(str3)
# print(str4)
# print(str5)
# print(str6)
# print(str7)

textFile.writelines(textFinal)
