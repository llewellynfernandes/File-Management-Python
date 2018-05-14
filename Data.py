import csv
import os


with open('result.csv', 'r') as result: #open the file with the data and asiign it to variable result
    csv_reader = csv.reader(result) #load result into csv.reader

#create new file to sort columns
    with open('sorted.csv', 'w') as sorted: #create and open file to write data
        csv_writer = csv.writer(sorted, delimiter='\t') #converting the csv to tab separated values
        for line in csv_reader: #writes each line at a time
            csv_writer.writerow(line) #write line

#adding empty columns to sorted.csv file
with open('sorted.csv', 'r') as sorted, open('result.csv', 'w') as result: #adding additional columns to the file
   reader = csv.reader(sorted, delimiter='\t')
   writer = csv.writer(result, delimiter='\t')
   for row in reader:
     writer.writerow(['', row[1], row[0], row[2], '', '', '', '', row[4], row[3]]) # '' added for each new column

# sorting columns
with open('result.csv', 'r') as result, open ('sorted.csv', 'w') as sorted:
    reader = csv.reader(result, delimiter='\t')
    writer = csv.writer(sorted, delimiter='\t')
    for row in reader:
      writer.writerow([row[0], row[1], row[3], row[2], row[4], row[5], row[6], row[7], row[8], row[9]])# columns can be sorted by shuffling the rows as desired

# sorting columns
with open('sorted.csv', 'r') as sorted, open('result.txt', 'w') as result:
   reader = csv.reader(sorted, delimiter='\t')
   writer = csv.writer(result, delimiter='\t')
   for row in reader:
       writer.writerow([row[0], row[1], row[2], row[8], row[4], row[5], row[6], row[7], row[3], row[9]]) # columns can be sorted by shuffling the rows as desired

#3 iterations of row sorting run, 'with' statement used since the file has to be closed after every iteration.

#Remove the header of the newly generated data file to append it to already existing data
with open('result.txt', 'r') as result:
    data = result.read().splitlines(True)
with open('result.txt', 'w') as result:
    result.writelines(data[1:])


#append the old file with new generated data file
#filenames = ['rnainfo2.txt', 'result.txt'] #link both files to variable
#with open('rnainfo.txt', 'w') as outfile: #set file as write
#    for fname in filenames:
#        with open(fname) as infile:
#            for line in infile:
#                outfile.write(line)


#Delete additional generated files
#try:
#    os.remove("sorted.csv")
#    os.remove("result.csv")
    #os.remove("result.txt")
#except OSError:
#    pass
