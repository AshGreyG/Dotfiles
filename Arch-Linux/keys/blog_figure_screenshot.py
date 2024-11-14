import os
import time
import shutil
import pyperclip

def move(src_path : str, dst_path : str) -> None :
    previous_files = set(os.listdir(src_path))
    
    while True :
        time.sleep(5)
        curent_files = set(os.listdir(src_path))
        added_files = curent_files - previous_files
        img_str = ""
        for file in list(added_files) :
            src_file = os.path.join(src_path, file)
            dst_file = os.path.join(dst_path, file)
            print(f"Move {src_file}\nto {dst_file}")
            img_str += "![](figure/" + file + ")\n"
            shutil.copy(src_file, dst_path)
            os.remove(src_file)
        if added_files :
            pyperclip.copy(img_str)
        previous_files = set(os.listdir(src_path))

if __name__ == "__main__" :
    src = r"/home/ashgrey/Pictures/Screenshot"
    dst = r"/home/ashgrey/Github/Blog-Picbed/figure"
    move(src, dst)