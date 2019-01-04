import os
import glob
my_path =r"D:\UTA Classes\Sem III"

pic_list = os.path.join(my_path,"*.jpg")

all_path_directory = glob.glob(pic_list)

for jpglist in all_path_directory:

    converted_file_name = jpglist[0:len(jpglist)-4] + ".png"
    os.rename(jpglist,converted_file_name)
        
print(os.listdir(my_path))

