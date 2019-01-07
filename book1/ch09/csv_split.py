#Splitting a CSV file by taking three required command line arguments
import sys
import os
import csv
import argparse
import time
"""
Splits a CSV file into mutiple files using command line arguments

    Arguments used:
    '-h' : help file of usage of the script
    '-i' : input file name
    '-o' : output_file_name
    '-r' : row limit to split

    Example usage:

    '''
    >> python csv_split.py -i input.csv -o output -r 100 ( splits csv by 100 rows)
    '''
"""

def get_argument():
    #Using argparse to get commandline arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", help = "csv input file(with extention)", type=str)
    parser.add_argument("-o", "--output_file",  help = "csv input file(with extention)", type = str)
    parser.add_argument("-r", "--row_limit", help = "csv input file(with extention)", type = int)
    args = parser.parse_args()

    #check weather the file exits or not
    is_file(parser, args.input_file)

    is_valid_row(parser,args.input_file, args.row_limit)

    return args.input_file, args.output_file, args.row_limit



def is_file(parser, file_name):
    # To check if the file exits
  
    if not os.path.exists(file_name):
        parser.error("The file '{}' does not exist".format(file_name))
        sys.exit(1)
    

def is_valid_row(parser,input_file_name, row_limit):
    row_count = 0 
    #count the no. of row
    for rows in csv.reader(open(input_file_name)):
        row_count+=1
    if row_count < row_limit:
        parser.error("The row limit exceeds the no of rows in file '{}'".format(input_file_name))
        sys.exit(1)
        

def split(arg):

    input_file = arg[0]
    output_file = arg[1]
    row_limit = arg[2]
    output_path = '.'
    lis =[]
    csv_opener = open(input_file,"r")
    with csv_opener as my_files:
        my_file_reader = csv.reader(my_files)

        for row in my_file_reader:
            lis.append(row)
        #Splitting the list of list into chunks of lenght row_limit
        for i in range(0,len(lis),row_limit):
            chunk = lis[i:i + row_limit] # Creates a single chunk

            ts = str(time.time())
            output_name = os.path.join(output_path,"{}.csv".format(ts)) #joining names and path
            csv_writer = open(output_name,"w")
            with csv_writer as my_file:
                my_file_writer = csv.writer(my_file)
                my_file_writer.writerows(chunk)
            print ("Filepath: {}".format(output_name))

if __name__ == "__main__":
    argument = get_argument()
    split(argument)
                
