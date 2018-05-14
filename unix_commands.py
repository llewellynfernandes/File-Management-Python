import os

#the unix command must be within "" and {} can be used for adding more parameters
#these few commands can be helpful when working with data, to clean it.

#run awk command in python
os.system("awk '!/Text/ {print}' txt_file.txt > new_file.txt") #read all lines in txt_file that contain Text in it and exlude them and write in new_file

#run sort command in python
os.system("sort -k1 -n txt_file.txt > new_file.txt") #Sort txt_file and write it to new_file

#run uniq command in python
os.system("uniq txt_file.txt > new_file.txt") #print unique values from txt_file to new_file
