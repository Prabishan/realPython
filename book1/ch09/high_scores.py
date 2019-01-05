#High Score List from a CSV Data
import os
import csv
my_path =r"C:\Users\Prabishan\Desktop\realPython\realPython\book1\ch09"
std_dict ={}
with open(os.path.join(my_path,"scores.csv"),"r") as my_files:

    my_file_reader = csv.reader(my_files)
    for name,score in my_file_reader:
        std_dict[name] = score

for name in sorted(std_dict):
    print(name,std_dict[name])
