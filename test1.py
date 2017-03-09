import csv

#with open("train.csv","r") as f:
#	r = csv.reader(f,delimiter=',')
#	for row in r:
#		if len(row)>= 2:
#
#			pr (row[0]+','+row[1])

with open("train.csv", "r") as infile, open("outfile.csv", "w") as outfile:
    reader = csv.reader(infile, delimiter=",")
    headers=next(reader,None)
    writer = csv.writer(outfile, delimiter=",")
    if headers:
    	writer.writerow(headers)
    for row in reader:
        row[21] = "200" 
        writer.writerow(row)
