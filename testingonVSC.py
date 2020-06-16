import csv

with open("data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line=0
    highest_firespots=0
    month=""
    state=""
    for row in csv_reader:
        if line!=0:
            if row[0]=="2019":
                if int(row[5])>highest_firespots:
                    highest_firespots=int(row[5])
                    month=row[1]
                    state=row[2]
        line += 1                
    
    print(highest_firespots)
    print("The month with the highest firespots [{}], was {} on {}".format(highest_firespots,month,state))
    print("I've processed {} lines to provide this information.".format(line))


