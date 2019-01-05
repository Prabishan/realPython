#Using pattern matching to delete files
import os
import glob

my_path=r"C:\Users\Prabishan\Desktop\realPython\realPython\book1\ch09\little pics"

for current_folder, subfolder, file_names in os.walk(my_path):
    for file in file_names:
        all_files = os.path.join(current_folder,file)
        if all_files[len(all_files)-4:len(all_files)]==".jpg":
            file_size = os.path.getsize(all_files)
            if file_size < 2000:
                print("{} deleting",all_files)
                os.remove(all_files)
                
