import os
import time
from PIL import Image

def move(src_path : str, dst_path : str) -> None :
    previous_files = set(os.listdir(src_path))
    count = 0
    for existed_file in os.listdir(dst_path) :
        name = existed_file[:existed_file.find(".")]
        if (int(name[6:]) >= count) :
            count = int(name[6:]) + 1
    
    while True :
        time.sleep(5)
        current_files = set(os.listdir(src_path))
        added_files = current_files - previous_files
        for file in list(added_files) :
            src_file = os.path.join(src_path, file)
            try : 
                dst_file = dst_path + "/image-" + str(count) + ".webp"
                with Image.open(src_file) as img :
                    img.save(dst_file, format="WEBP", quality=100)
                print(f"Move {src_file}\nto {dst_file}")
            except Exception as e :
                print(f"Error : {e}")
            os.remove(src_file)
            previous_files = set(os.listdir(src_path))
            count = count + 1

if __name__ == "__main__" :
    src = r"/home/ashgrey/Pictures/Screenshot/"
    dst = r"/home/ashgrey/Github/Blog-Bicbed/image/"
    move(src, dst)