my_output_file = open("hello.txt","w")
my_output_file.writelines("Hello This is Prabishan\nI am from C-137")
my_output_file.close()
my_read_file = open("hello.txt","r")
for lines in my_read_file.readlines():
    print(lines,end=""),
my_read_file.close()
