from zipfile import ZipFile
import os
from pathlib import Path
import shutil


def unzip_all_files():
        dir = os.getcwd()
        files = os.listdir(dir)
        for file in files:
                if Path(file).suffix == '.zip':
                        with ZipFile(file, 'r') as z:
                                z.extractall()



def move_all_files(old_dir, new_dir):
        files = os.listdir(os.chdir(old_dir))
        new_location = Path(new_dir)
        for file in files:
                shutil.move(file, new_location)




